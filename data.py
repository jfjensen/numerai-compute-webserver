import numerox as nx
import numerapi
import config as cfg

dataset_file = 'numerai_dataset.zip'

def get_data():
    napi = numerapi.NumerAPI()
    current_round = napi.get_current_round()

    data_up_to_date = True
    config = cfg.load_config()    

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
        data = nx.load_zip(dataset_file)
    else:
        # dataset is not up to date
        # download latest dataset from numerai
        print("tournament data being downloaded...")
        data = nx.download(dataset_file)
        # our data is now up to date so we save the latest round number
        config['persistence']['saved_round'] = current_round
        cfg.save_config(config)
        data_up_to_date = True

    return data