import numerox as nx
import numerapi
import os
import model
import data as dt


def train():

    tournaments = nx.tournament_names()
    print(tournaments)

    data = dt.get_data()

    for tournament_name in tournaments:
        # create your model
        m = model.LogisticModel(verbose=True)

        print("fitting model for", tournament_name)
        m.fit(data['train'], tournament_name)

        print("saving model for", tournament_name)
        m.save('model_trained_' + tournament_name)
