Voici le résultat du projet qui nous a été commissionné par Olist, une entreprise brésilienne qui propose une solution de vente sur les marketplaces en ligne. Le but de notre mission était de réaliser une segmentation clients et de  faire une prédiction sur les frais de livraison et les délais de livraison des articles. Le but final est d'avoir une application web avec une interface de restitution en local et une base de données qui s'alimente à chaque utilisation de l'application.

## Procédure d'installation
- Si ce n'est pas déjà fait, [installez Python](https://www.python.org/downloads/)
- Dans le dossier du projet, ouvrez un invite de commandes et tapez la commande suivante : `pip install -r requirements.txt`
- Enfin, installez Jupyter Lab (`pip install jupyterlab`) ou Jupyter Notebook (`pip install notebook`) afin de pouvoir ouvrir les notebooks.

## Structure du projet
- Le dossier INTERFACE contient tous les scripts permettant de lancer l'interface graphique du projet
- PREDICTION freight_value et PREDICTION_delivery contiennent le code permettant de prédire les frais de port et les délais de livraison de commande passées sur Olist
- SEGMENTATION_CLIENTS contient le code qui permet de réaliser une segmentation des clients selon la méthode RFM (Recency, Frequency, Monetary analyses)


