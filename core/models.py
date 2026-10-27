from django.db import models


TYPE_TRANS_CHOICES = (
    ('retrait', 'retrait'),
    ('depot', 'depot'),
)

ROLES = (
    ('AGENT_COMMERCIAL', 'AGENT_COMMERCIAL'),
    ('DIRECTEUR_COMMERCIAL', 'DIRECTEUR_COMMERCIAL'),
)

STATUS_CREDIT = (
    ('EN ATTENTE', 'EN ATTENTE'),
    ('APPROUVE', 'APPROUVE'),
    ('REJETE', 'REJETE'),
)

TYPE_CREDIT = (
    ('INVEST', 'INVEST'),
    ('ACADEMIA', 'ACADEMIA'),
    ('SANTE', 'SANTE'),
    ('IMMO', 'IMMO'),
)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom_complet = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    revenuMensuel = models.DecimalField(max_digits=12, decimal_places=2)
    employeur = models.CharField(max_length=200)
    telephone = models.CharField(max_length=13, unique=True)
    genre = models.PositiveSmallIntegerField()
    adresse = models.TextField()
    date_naissance = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_complet} | {self.genre} | {self.adresse}"


class Compte(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10, unique=True)
    solde = models.DecimalField(max_digits=12, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='comptes')

    def __str__(self):
        return f"Compte {self.numero}"


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(
        choices=TYPE_TRANS_CHOICES,
        default='depot',
        max_length=30,
    )
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, related_name='transactions')


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    nom_complet = models.CharField(max_length=200)
    actif = models.BooleanField(default=True)
    roles = models.CharField(choices=ROLES, default='AGENT_COMMERCIAL', max_length=200)

    def __str__(self):
        return self.nom_complet


class DemandeCredit(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    duree = models.IntegerField()
    type = models.CharField(choices=TYPE_CREDIT, default='INVEST', max_length=100)
    status = models.CharField(choices=STATUS_CREDIT, default='EN ATTENTE', max_length=100)
    date_cloture = models.DateField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, related_name='demandes_credit')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='demandes_credit')

    def __str__(self):
        return f"Demande {self.id} - {self.montant}"


class Remboursement(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    demandeCredit = models.ForeignKey(DemandeCredit, on_delete=models.CASCADE, related_name='remboursements')

    def __str__(self):
        return f"Remboursement {self.id} - {self.montant}"