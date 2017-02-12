from __future__ import unicode_literals

from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=100)

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


class Election(models.Model):
    year = models.IntegerField()
    office = models.CharField(choices=OFFICES, max_length=30)
    district = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return '%s %s - %s' % (self.state, self.office, self.year)


class ElectionCandidate(models.Model):
    candidate = models.ForeignKey(Candidate)
    election = models.ForeignKey(Election)
    party = models.ForeignKey(Party)
    incumbent = models.BooleanField()
    general_votes = models.IntegerField()
    winner = models.BooleanField()
    fec_id = models.CharField(max_length=30, blank=True)

    # def __str__(self):
    #     string = '%s %s' % (
    #         self.candidate.first_name,
    #         self.candidate.last_name,
    #     )
    #     if self.winner:
    #         string = '%s - Winner' % (string)
    #     return string
