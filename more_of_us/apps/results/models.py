from __future__ import unicode_literals
from django.db import models
from django.db.models import Q, Count


class Party(models.Model):
    name = models.CharField(max_length=100)
    major = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # def __str__(self):
    #     return '%s %s' % (self.first_name, self.last_name)


OFFICES = (
    ('sen', 'SENATOR'),
    ('rep', 'CONGRESSMAN'),
    ('pres', 'PRESIDENT')
)

DEM_AFFILIATED_PARTIES = [
    'D',
    'D*',
    'IFM',
    'DFL',
    'DNL',
    'D/WF/IDP Combined Parties',
    'D/IND',
    'WF'
]


class Election(models.Model):
    year = models.IntegerField()
    office = models.CharField(choices=OFFICES, max_length=30)
    district = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    runoff = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s - %s' % (
            self.state, self.office, self.district, self.year)

    @property
    def winner(self):
        try:
            return self.electioncandidate_set.get(winner=True)
        except ElectionCandidate.MultipleObjectsReturned:
            # Due to same candidate listed w/ multiple parties (e.g., WF & D)
            duplicate_winners = self.electioncandidate_set.filter(winner=True)
            return duplicate_winners.get(party__major=True)


class ElectionCandidate(models.Model):
    candidate = models.ForeignKey(Candidate)
    election = models.ForeignKey(Election)
    party = models.ForeignKey(Party)
    incumbent = models.BooleanField()
    votes = models.IntegerField()
    winner = models.BooleanField()
    fec_id = models.CharField(max_length=30, blank=True)
    combined_parties = models.BooleanField(default=False)

    # def __str__(self):
    #     string = '%s %s' % (
    #         self.candidate.first_name,
    #         self.candidate.last_name,
    #     )
    #     if self.winner:
    #         string = '%s - Winner' % (string)
    #     return string

    @classmethod
    def dem_winners_by_office(cls, office):

        senate_winners = ElectionCandidate.objects.filter(
            election__office=office, winner=True)
        senate_winners = senate_winners.filter(
            party__name__in=DEM_AFFILIATED_PARTIES)

        # Because the FEC marks some elections as having more than 1 winner
        # if the candidate is affilaited with more than 1 party, we have
        # to go through are remove those while leaving the "major" party
        # winner.
        dups = (
            senate_winners.values('fec_id')
            .annotate(count=Count('id'))
            .values('fec_id')
            .order_by()
            .filter(count__gt=1)
        )
        senate_winners = senate_winners.exclude(
            fec_id__in=dups, party__major=False)

        return senate_winners
