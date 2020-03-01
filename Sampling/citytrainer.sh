rm san_francisco_random.csv
rm san_diego_random.csv
rm los_angeles_random.csv
rm san_francisco_stratified.csv
rm san_diego_stratified.csv
rm los_angeles_stratified.csv

python3 RandomSampling.py sf 6000
python3 RandomSampling.py sd 6000
python3 RandomSampling.py la 6000

python3 StratifiedSampling.py sf 6000 1 3
python3 StratifiedSampling.py sd 6000 1 3
python3 StratifiedSampling.py la 6000 1 3

# python3 ReservoirSampling.py sf 6000
# python3 StratifiedSampling.py sd 6000
# python3 StratifiedSampling.py la 6000
