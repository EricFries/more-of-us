import sys, os
import csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "more_of_us.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from more_of_us.apps.results.models import (
    Party, Candidate, Election,
    ElectionCandidate)


elections = [
    {
        'state': 'AL',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Richard',
                'last_name': 'Shelby',
                'incumbent': True,
                'votes': 1323184,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Ron',
                'last_name': 'Crumpton',
                'incumbent': False,
                'votes': 737542,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'AK',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Lisa',
                'last_name': 'Murkowski',
                'incumbent': True,
                'votes': 111382,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Ray',
                'last_name': 'Metcalfe',
                'incumbent': False,
                'votes': 28026,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'AZ',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'John',
                'last_name': 'McCain',
                'incumbent': True,
                'votes': 1089324,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Ann',
                'last_name': 'Kirkpatrick',
                'incumbent': False,
                'votes': 839542,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'AR',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'John',
                'last_name': 'Boozman',
                'incumbent': True,
                'votes': 657856,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Conner',
                'last_name': 'Eldridge',
                'incumbent': False,
                'votes': 397970,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'CA',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Loretta',
                'last_name': 'Sanchez',
                'incumbent': False,
                'votes': 3918486,
                'winner': False,
                'party': 'D'
            },
            {
                'first_name': 'Kamala',
                'last_name': 'Harris',
                'incumbent': False,
                'votes': 6495907,
                'winner': True,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'CO',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Michael',
                'last_name': 'Bennet',
                'incumbent': True,
                'votes': 1246357,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Darryl',
                'last_name': 'Glenn',
                'incumbent': False,
                'votes': 1149326,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'CT',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Richard',
                'last_name': 'Blumenthal',
                'incumbent': True,
                'votes': 986291,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Dan',
                'last_name': 'Carter',
                'incumbent': False,
                'votes': 546489,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'FL',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Marco',
                'last_name': 'Rubio',
                'incumbent': True,
                'votes': 4822182,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Patrick',
                'last_name': 'Murphy',
                'incumbent': False,
                'votes': 4105251,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'GA',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Johnny',
                'last_name': 'Isakson',
                'incumbent': True,
                'votes': 2110737,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Jim',
                'last_name': 'Barksdale',
                'incumbent': False,
                'votes': 1565006,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'HI',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Brian',
                'last_name': 'Schatz',
                'incumbent': True,
                'votes': 306543,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'John',
                'last_name': 'Carroll',
                'incumbent': False,
                'votes': 92620,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'ID',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Michael',
                'last_name': 'Crapo',
                'incumbent': True,
                'votes': 447342,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Jerry',
                'last_name': 'Sturgill',
                'incumbent': False,
                'votes': 188104,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'IL',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Tammy',
                'last_name': 'Duckworth',
                'incumbent': True,
                'votes': 2908363,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Mark',
                'last_name': 'Kirk',
                'incumbent': True,
                'votes': 2150099,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'IN',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Todd',
                'last_name': 'Young',
                'incumbent': False,
                'votes': 1423001,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Evan',
                'last_name': 'Bayh',
                'incumbent': False,
                'votes': 1157799,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'IA',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Chuck',
                'last_name': 'Grassley',
                'incumbent': True,
                'votes': 923280,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Patty',
                'last_name': 'Judge',
                'incumbent': False,
                'votes': 546974,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'KS',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Jerry',
                'last_name': 'Moran',
                'incumbent': True,
                'votes': 716661,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Patrick',
                'last_name': 'Wiesner',
                'incumbent': False,
                'votes': 368672,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'KY',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Rand',
                'last_name': 'Paul',
                'incumbent': True,
                'votes': 1090151,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Jim',
                'last_name': 'Gray',
                'incumbent': False,
                'votes': 813222,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'LA',
        'runoff': True,
        'candidates': [
            {
                'first_name': 'Foster',
                'last_name': 'Campbell',
                'incumbent': False,
                'votes': 347813,
                'winner': False,
                'party': 'D'
            },
            {
                'first_name': 'John',
                'last_name': 'Kennedy',
                'incumbent': False,
                'votes': 536204,
                'winner': True,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'MD',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Chris',
                'last_name': 'Van Hollen',
                'incumbent': False,
                'votes': 1488845,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Kathy',
                'last_name': 'Szeliga',
                'incumbent': False,
                'votes': 898902,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'MO',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Roy',
                'last_name': 'Blunt',
                'incumbent': True,
                'votes': 1370240,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Jason',
                'last_name': 'Kander',
                'incumbent': True,
                'votes': 1283222,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'NV',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Catherin',
                'last_name': 'Cortez Maso',
                'incumbent': False,
                'votes': 520658,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Joe',
                'last_name': 'Heck',
                'incumbent': False,
                'votes': 494427,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'NH',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Maggie',
                'last_name': 'Hassan',
                'incumbent': False,
                'votes': 354268,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Kelly',
                'last_name': 'Ayotte',
                'incumbent': True,
                'votes': 353525,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'NY',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Chuck',
                'last_name': 'Schumer',
                'incumbent': True,
                'votes': 4788374,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Wendy',
                'last_name': 'Long',
                'incumbent': False,
                'votes': 1865072,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'NC',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Richard',
                'last_name': 'Burr',
                'incumbent': True,
                'votes': 2371191,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Deborah',
                'last_name': 'Ross',
                'incumbent': False,
                'votes': 2102666,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'ND',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'John',
                'last_name': 'Hoeven',
                'incumbent': True,
                'votes': 267964,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Eliot',
                'last_name': 'Glassheim',
                'incumbent': False,
                'votes': 57976,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'OH',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Rob',
                'last_name': 'Portman',
                'incumbent': True,
                'votes': 3048467,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Ted',
                'last_name': 'Strickland',
                'incumbent': False,
                'votes': 1929873,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'OK',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'James',
                'last_name': 'Lankford',
                'incumbent': True,
                'votes': 979728,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Mike',
                'last_name': 'Workman',
                'incumbent': False,
                'votes': 355389,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'OR',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Ron',
                'last_name': 'Wyden',
                'incumbent': True,
                'votes': 1038632,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Mark',
                'last_name': 'Callahan',
                'incumbent': False,
                'votes': 616203,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'PA',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Patrick',
                'last_name': 'Toomy',
                'incumbent': True,
                'votes': 2893833,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Katie',
                'last_name': 'McGinty',
                'incumbent': False,
                'votes': 2793668,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'SC',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Tim',
                'last_name': 'Scott',
                'incumbent': True,
                'votes': 1228844,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Thomas',
                'last_name': 'Dixon',
                'incumbent': False,
                'votes': 752001,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'SD',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'John',
                'last_name': 'Thune',
                'incumbent': True,
                'votes': 265494,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Jay',
                'last_name': 'Williams',
                'incumbent': False,
                'votes': 104125,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'UT',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Mike',
                'last_name': 'Lee',
                'incumbent': True,
                'votes': 659769,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Misty',
                'last_name': 'Snow',
                'incumbent': False,
                'votes': 265674,
                'winner': False,
                'party': 'D'
            },
        ]
    },
    {
        'state': 'VT',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Patrick',
                'last_name': 'Leahy',
                'incumbent': True,
                'votes': 191855,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Scott',
                'last_name': 'Milne',
                'incumbent': False,
                'votes': 103266,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'WA',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Patty',
                'last_name': 'Murray',
                'incumbent': True,
                'votes': 1765333,
                'winner': True,
                'party': 'D'
            },
            {
                'first_name': 'Chris',
                'last_name': 'Vance',
                'incumbent': False,
                'votes': 1220755,
                'winner': False,
                'party': 'R'
            },
        ]
    },
    {
        'state': 'WI',
        'runoff': False,
        'candidates': [
            {
                'first_name': 'Ron',
                'last_name': 'Johnson',
                'incumbent': True,
                'votes': 1478170,
                'winner': True,
                'party': 'R'
            },
            {
                'first_name': 'Russ',
                'last_name': 'Feingold',
                'incumbent': False,
                'votes': 1378922,
                'winner': False,
                'party': 'D'
            },
        ]
    },
]


for election in elections:
    new_election = Election(
        year=2016,
        office='sen',
        state=election['state']
    )
    new_election.save()

    for candidate in election['candidates']:
        new_candidate, created = Candidate.objects.get_or_create(
                first_name=candidate['first_name'],
                last_name=candidate['last_name'])
        party, created = Party.objects.get_or_create(
            name=candidate['party']
        )
        election_candidate = ElectionCandidate(
            candidate=new_candidate,
            election=new_election,
            party=party,
            incumbent=candidate['incumbent'],
            votes=candidate['votes'],
            winner=candidate['winner'],
            fec_id='',
            combined_parties=False
            )
        election_candidate.save()
