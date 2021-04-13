import oyaml as yaml
import os

with open(f"./priority_list.yaml",'r') as priority:
    priority_list = yaml.load(priority)

print(priority_list)

all_tx_data = []
all_rx_data = []

for file in os.listdir('./mini_yamls'):
    with open(f"./mini_yamls/{file}", 'r') as yaml_file:
        data = yaml.load(yaml_file)
    data_tx = data["MessagesTX"]
    data_rx = data["MessagesRX"]

    all_tx_data.append(data_tx)
    all_rx_data.append(data_rx)

print(all_rx_data)

yaml_out_tx = {"MessagesTX": all_tx_data}
yaml_out_rx = {"MessagesRX": all_rx_data}

with open(f'./mega.yaml', 'w+') as file:
    yaml.dump(yaml_out_tx, file)
    yaml.dump(yaml_out_rx, file)
