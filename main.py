from straw_hat import StrawHatTreasury
from treasure import Treasure

# Create an instance of StrawHatTreasury
treasury = StrawHatTreasury(m=50)

# Open a file in write mode
with open('completion_times.txt', 'w') as file:
    # First treasure addition
    for i in range(1, 500):
        treasury.add_treasure(Treasure(i, 3 * i + 2, 4 * i - 1))

    # Write first call completion times
    file.write("First Call\n")
    l = treasury.get_completion_time()
    for i in l:
        file.write(f"{i.completion_time}\n")      

    # Second treasure addition
    for i in range(500, 1000):
        treasury.add_treasure(Treasure(i, 3 * i - 500, 4 * i - 1))

    # Write second call completion times
    file.write("Second Call\n")
    l = treasury.get_completion_time()
    for i in l:
        file.write(f"{i.completion_time}\n")
