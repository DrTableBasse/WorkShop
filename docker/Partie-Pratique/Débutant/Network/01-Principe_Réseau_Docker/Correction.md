# Correction de l'exercice sur les Réseaux Docker pour Débutants
## 1. Création du réseau "mon_reseau"

```bash
docker network create --subnet=172.18.0.0/16 mon_reseau
```

## 2. Lancement des conteneurs

```bash
docker run -d --name nginx1 --network mon_reseau --ip 172.18.0.10 nginx
docker run -d --name mysql1 --network mon_reseau --ip 172.18.0.11 mysql
```

## 3. Vérification de la connectivité au réseau

```bash
docker network inspect mon_reseau
```
Assurez-vous que les deux conteneurs (nginx1 et mysql1) sont répertoriés dans la section "Containers".

## 4. Vérification de la connectivité entre les conteneurs

```bash
docker exec nginx1 ping 172.18.0.11
docker exec mysql1 ping 172.18.0.10
```
Assurez-vous qu'il n'y a pas de perte de paquets, indiquant une connectivité réussie.

## 5. Suppression du réseau et des conteneurs

```bash
docker network rm mon_reseau
docker rm -f nginx1 mysql1
```

Assurez-vous que tous les conteneurs et le réseau ont été supprimés avec succès.