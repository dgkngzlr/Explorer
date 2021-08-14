import glob
import json
import os



def is_org_exist(exp_path):

    exp_folder = glob.glob(explorer_path+"*")

    for _ in exp_folder:

        if "organization" in _:
            return True
        else:
            return False

# Get sk name
keystore_path = "./organizations/peerOrganizations/org1.example.com/users/User1@org1.example.com/msp/keystore/"
sk = glob.glob(keystore_path+"*")[0].split("/")[-1]
print("sk :", sk)

# Open .json file
json_path = "./connection-profile/test-network.json"
with open(json_path, "r") as f:

    data = f.read()

# .json as dict
test_network = json.loads(data)

# Swap sk
old_sk = test_network["organizations"]["Org1MSP"]["adminPrivateKey"]["path"]
print("old_sk :", old_sk)
new_sk = old_sk[0:old_sk.rindex("/")+1] + sk
print("new_sk :", new_sk)
test_network["organizations"]["Org1MSP"]["adminPrivateKey"]["path"] = new_sk

new_json = str(json.dumps(test_network, indent=4))

# Open .json file
json_path = "./connection-profile/test-network.json"
with open(json_path, "w") as f:

    data = f.write(new_json)

print("Succesfull !")

