rm data.csv
rm SuccessiveSample.sh
touch data.csv
for i in {4..100}
do
  echo "python3 Oversample.py sf 6000 $i" >> SuccessiveSample.sh
done

chmod 744 SuccessiveSample.sh
./SuccessiveSample.sh
