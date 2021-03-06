import sys, os
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "more_of_us.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from more_of_us.apps.results.models import (
    Party, Candidate, Election,
    ElectionCandidate)

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'senate_results_14.csv')


def is_a_general_candidate_row(fec_id):
    return fec_id not in ['n/a', '', 'FEC ID#']


def has_runoff_votes(runoff_votes):
    if runoff_votes:
        return True
    return False


def is_combined_party_election_candidate(combined_party_votes):
    if combined_party_votes:
        return True
    return False


def format_vote_total(string_votes):
    string_votes = votes.replace(',', '')
    return int(string_votes)


def is_special_election(district_description):
    return 'unexpired' in district_description.lower()


def is_major_party(party_name):
    return party_name in ['R', 'D', 'D*']


with open(file_path, 'rb') as csvfile:
    results = csv.reader(csvfile, delimiter=',')

    for row in results:
        try:
            fec_id = row[3].strip()
        except IndexError:
            continue

        if not is_a_general_candidate_row(fec_id):
            continue

        district_description = row[2].strip()
        if is_special_election(district_description):
            continue

        runoff_votes = row[12].strip()
        party_name = row[9].strip()
        combined_party_votes = row[18].strip()
        if has_runoff_votes(runoff_votes):
            votes = runoff_votes
        elif is_combined_party_election_candidate(combined_party_votes):
            votes = combined_party_votes
        else:
            general_votes = row[14].strip()
            votes = general_votes

        try:
            votes = format_vote_total(votes)
        except:
            continue
        print party_name
        party, created = Party.objects.get_or_create(
            name=party_name
            )

        if created:
            party.major = is_major_party(party_name)
            party.save()

        first_name = row[5].strip()
        last_name = row[6].strip()

        print first_name + ' ' + last_name

        candidate, created = Candidate.objects.get_or_create(
                first_name=first_name,
                last_name=last_name)

        state = row[1].strip()

        election, created = Election.objects.get_or_create(
            year=2014,
            district=district_description,
            office='sen',
            state=state,
            )

        # skip rows where the eleciton is a runoff but candidate
        # did not get runoff votes.
        if not created and election.runoff and \
           not has_runoff_votes(runoff_votes):
            continue

        election.runoff = has_runoff_votes(runoff_votes)
        election.save()

        incumbent = row[4] == '(I)'

        outcome = row[20].strip()
        mark_as_winner = 'w' in outcome.lower()

        election_candidate = ElectionCandidate(
            candidate=candidate,
            election=election,
            party=party,
            incumbent=incumbent,
            votes=int(votes),
            winner=mark_as_winner,
            fec_id=fec_id,
            combined_parties=is_combined_party_election_candidate(party_name)
            )
        election_candidate.save()
