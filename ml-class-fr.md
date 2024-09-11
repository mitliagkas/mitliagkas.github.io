---
layout: default
title: ML class
menu: main
permalink: /ml-class-fr/
order: 3
---

IFT3395/IFT6390A: Fondements de l'apprentissage machine -- Automne 2024 -- donné en presentiel
=========

Un cours d'introduction mais **très intensif** en apprentissage automatique.

**REMARQUE:
In the fall semester of 2024 I am teaching the french section of the class, IFT6390A, as well as the undergraduate class, IFT3395.
My colleague, Dhanya Sridhar, will teach the english section, IFT6390B.

Les cours et les travaux pratiques sont donnés en français.
Les devoirs et les examens seront disponibles en français et en anglais. 
Les étudiants sont toujours encouragés à soumettre leur travail et à poser des questions dans la langue de leur choix.

**IMPORTANT :
Veuillez ne vous inscrire à ce cours qu'après avoir lu et examiné attentivement toutes les conditions requises énumérées dans la page [prerequisites](/ml-class-prerequisites-fr).**


Ressources
--------- 
Nous ajouterons tous les étudiants inscrits à Piazza et Gradescope.
Vous recevrez des invitations et des annonces à l'adresse électronique associée à votre inscription. 
Pour la majorité d'entre vous, il s'agit d'une adresse de courriel qui se termine par @umontreal.ca. 
Vous devriez pouvoir y accéder [ici](https://outlook.umontreal.ca/) avec vos identifiants UdeM/Synchro. 

**IMPORTANT : Veillez à apprendre à utiliser cette boîte aux lettres électronique et à la consulter souvent. Nous ne pourrons pas vous ajouter en utilisant d'autres adresses électroniques**.


Participation sans inscription
--------
Si vous souhaitez suivre le cours, veuillez remplir ce [formulaire](https://forms.gle/RUJQYevmrfsh9AMD8). 
Vous aurez accès au matériel de cours, mais vous ne pourrez pas soumettre votre travail sur Gradescope ni être noté. 


Communication
------------- 

Toute notre communication se fera via la page Piazza de la classe. 
Les étudiants inscrits seront automatiquement ajoutés à la page Piazza la veille du premier cours. 

La soumission et l'évaluation des devoirs se feront sur Gradescope. Vous serez invité à accéder à la page Gradescope de la classe automatiquement la veille du début des cours. Si vous êtes auditeur libre, vous ne serez pas ajouté à Gradescope et vous ne pourrez pas soumettre vos devoirs.

**Important:** Assurez-vous d'apprendre à utiliser et de vérifier votre boîte de courriel @umontreal.ca. C'est là que vous recevrez les annonces et les invitations aux services en ligne de la classe.

Les classes ne seront utilisées que pour la coordination initiale avec les étudiants inscrits jusqu'à ce qu'ils aient accès à Piazza. Il n'y aura pas de discussions sur Studium. 

**Avis important sur la communication par email:**
Il s'agit d'une classe très nombreuse, l'instructeur ne sera donc pas en mesure de répondre aux questions individuelles sur le cours par courrier électronique.  **Exclusivement dans le cas où vous avez une question de nature sensible et personnelle:** N'hésitez pas à envoyer un courriel à l'instructeur.  Veuillez commencer l'objet de votre courriel par « [IFT6390] », sinon votre courriel risque d'être perdu.



Horaires des cours et des laboratoires
-----
Les cours de l'instructeur ont lieu
- mardi à 12h30-13h20 ET
- mercredi à 9h30-11h10 ET

Travaux pratiques hebdomadaires dirigés par un assistant enseignant le
- mardi à 13h30-15h30 ET

Des informations mises à jour peuvent toujours être trouvées en suivant les instructions ci-dessous « TROUVEZ L'HORAIRE D'UN COURS » au bas de <a href="https://admission.umontreal.ca/cours-et-horaires/cours/ift-6390/">
ce lien</a>.


Contenu et objectifs de la classe
------------------
Ce cours est une introduction à l'apprentissage machine (ML), un domaine de recherche en intelligence artificielle. L'objectif des algorithmes d'apprentissage automatique est de permettre à la machine d'apprendre à partir d'exemples. Le cours se concentre sur la classification et la régression : nous observons un ensemble de paires (observation, cible) où la cible est par exemple une classe et nous essayons de prédire la cible correspondant à une nouvelle observation. Les applications classiques de ces algorithmes se trouvent dans le domaine de la reconnaissance des formes (caractères, images, parole, etc.). Ces dernières années, plusieurs nouveaux champs d'application ont émergé : data mining, analyse statistique de données textuelles, gestion quantitative de portefeuilles financiers, analyse d'expressions génétiques, etc. Le sujet du cours peut être exploité dans de nombreux domaines de l'informatique.

Le cours couvrira les sujets suivants : notions générales (terminologie de base, généralisation, malédiction de la dimensionnalité, capacité, comparaison de classificateurs), algorithmes supervisés (k-voisins les plus proches, classificateurs linéaires, réseaux de neurones, machines à vecteurs de support, arbres de décision et régression, méthodes d'ensemble), algorithmes non supervisés (analyse en composantes principales, méthode des k-moyennes), aperçu des modèles graphiques probabilistes.

Notions couvertes (titres indicatifs) :
- Introduction et terminologie de l'apprentissage.
- Représentation des données (+ rappels d'algèbre linéaire).
- Les tâches d'apprentissage supervisé (classification, régression) et non supervisé (estimation de densité, clustering, réduction de dimensionnalité, ...).
- Méthodes basées sur les histogrammes. La malédiction de la dimensionnalité. (+ rappels de probabilités et de statistiques)
- Méthodes basées sur le voisinage (voisins les plus proches et fenêtres de Parzen)
- Densité gaussienne multivariée
- Cadre général de l'apprentissage, évaluation des performances, sélection des modèles, concept de capacité.
- Principe du maximum de vraisemblance et inférence bayésienne. Classificateur de Bayes.
- Régression et classification linéaire (régression logistique, perceptron, SVM linéaire, ...)
- Classification et régression non linéaire avec l'astuce du noyau (+ techniques d'optimisation)
- Classification et régression non linéaire : Réseaux de neurones de type MLP (+ révision du calcul des dérivées partielles)
- Architectures de réseaux de neurones plus avancés : convolutionnels, récurrents.
- Arbres de décision.
- Méthodes d'agrégation : bagging et boosting
- Apprentissage non supervisé : réduction de la dimensionnalité (ACP, ...). Partitionnement (k-means, ...)
- Aperçu des modèles graphiques probabilistes
- Introduction à l'apprentissage profond
- Réseaux neuronaux convolutifs
- Réseaux neuronaux récurrents

<h2>Labo</h2>
Voici un échantillon des trois premiers laboratoires de l'année dernière pour vous aider à démarrer jusqu'à ce que vous ayez accès au matériel de cette année.

- <a href="https://docs.google.com/presentation/d/1DB5-BGoImjcnsd1amnjQ4s4nhjUZhknCd5rra3eFnaU/edit?usp=sharing">Lab 0 Slides: Class tools (Thursday, September 5th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1XizC8QB33mAhG5FaenF5ILo8La4vdX-9/view?usp=sharing">Lab 1 Notebook: Numpy (Thursday, September 12th, 2019)</a> 
- <a href="https://drive.google.com/file/d/1odCUuWRKk6SBIGpQtkSBVdPErTQ_fEzy/view?usp=sharing">Lab 1 Notebook: k-NN (Thursday, September 12th, 2019)</a> 




<h2>Evaluation, IFT3395</h2>

**Quiz hebdomadaires (30%):**
Nous aurons un quiz hebdomadaire en ligne. Vous pourrez faire ce test de n'importe où.
Il consistera en de courtes questions sur le cours de la semaine dernière et sera administré sur Gradescope. 
Une fois que vous aurez commencé le quiz, vous aurez 15 minutes pour le terminer. 
Nous aurons au moins 12 quiz pendant le semestre ; vos 6 meilleurs scores seront utilisés pour calculer votre score semestriel aux quiz (10% de votre note finale).

**Devoirs (30%):**
3 séries de devoirs (10% chacune) comprenant des exercices théoriques, de la programmation et de l'expérimentation.
La plupart des devoirs seront soumis individuellement (chaque étudiant travaillant de son côté) et certains en équipe de deux.

**Compétitions de données (10%):**
Deux compétitions Kaggle.
La première couvrira la première moitié du cours et comptera pour 10% de votre note.
 et le second s'étendra sur la seconde moitié du cours et comptera pour 20% de votre note.

**Examen final (30%):**
Examen portant sur l'ensemble de la matière du cours à la fin du semestre. 
La date exacte et le format seront annoncés ultérieurement.


*Pour la plupart de ces évaluations, vous pourrez soumettre votre travail et voir vos notes sur Gradescope. 
 Voir la section 'Communication' pour plus d'informations sur l'accès. *


Fraude académique et plagiat
---------------- 

**ATTENTION:**
L'Université de Montréal a désormais une politique stricte en cas de fraude ou de plagiat.
Si une infraction est constatée, le professeur est tenu d'en faire rapport au directeur du département.
Une procédure administrative est alors automatiquement déclenchée avec les conséquences suivantes : l'infraction est notée dans votre dossier,
et une sanction est décidée (qui peut être grave et aller jusqu'au licenciement en cas de récidive). Il est important que vous fassiez le travail vous-même !



