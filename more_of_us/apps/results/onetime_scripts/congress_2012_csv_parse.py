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
file_path = os.path.join(module_dir, 'congress_results_2012.csv')


def is_a_general_candidate_row(fec_id):
    return fec_id not in ['n/a', '', 'FEC ID#'] \

with open(file_path, 'rb') as csvfile:
    results = csv.reader(csvfile, delimiter=',')

    for row in results:
        try:
            fec_id = row[3]
        except IndexError:
            continue

        try:
            string_votes = row[10].replace(',', '')
            general_votes = int(string_votes)
        except:
            continue

        if not is_a_general_candidate_row(fec_id):
            continue

        party, created = Party.objects.get_or_create(
            name=row[9]
            )

        first_name = row[5]
        last_name = row[6]
        candidate, created = Candidate.objects.get_or_create(
            first_name=first_name,
            last_name=last_name)

        state = row[1]
        district = row[2]
        office = 'sen'
        if district is not 'S':
            office = 'rep'
        candidate_is_winner = row[16] == 'W'
        election, created = Election.objects.get_or_create(
            year=2012,
            district=district,
            office=office,
            state=state,
            )

        election.save()

        incumbent = row[4] == '(I)'

        election_candidate = ElectionCandidate(
            candidate=candidate,
            election=election,
            party=party,
            incumbent=incumbent,
            general_votes=int(general_votes),
            winner=candidate_is_winner,
            fec_id=fec_id
            )
        election_candidate.save()


