import numerox as nx
import numerapi
import os
import model
import json

config_file = "config.json"

def train():
    data_up_to_date = True
    tournaments = nx.tournament_names()
    print(tournaments)

    napi = numerapi.NumerAPI()
    current_round = napi.get_current_round()

    config = None
    with open(config_file, "r") as read_file:
        config = json.load(read_file)
        # get the round number of the saved data
        saved_round = config['persistence']['saved_round']
        print("current_round: {}, saved_round: {}".format(current_round, saved_round))
        if saved_round < current_round:
            # if saved data is from a previous round then it is not up to date
            data_up_to_date = False

    data = None
    if data_up_to_date:
        # dataset is up to date
        # load dataset from file (no need to download it)
        print("loading tournament data from file...")
        data = nx.load_zip('numerai_dataset.zip')
    else:
        # dataset is not up to date
        # download latest dataset from numerai
        print("tournament data being downloaded...")
        data = nx.download('numerai_dataset.zip')
        # our data is now up to date so we save the latest round number
        config['persistence']['saved_round'] = current_round
        with open(config_file, "w") as write_file:
            json.dump(config, write_file)
        data_up_to_date = True


    for tournament_name in tournaments:
        # create your model
        m = model.LogisticModel(verbose=True)

        print("fitting model for", tournament_name)
        m.fit(data['train'], tournament_name)

        print("saving model for", tournament_name)
        m.save('model_trained_' + tournament_name)
