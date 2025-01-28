source .venv/bin/activate
python3 ./sm_parser.py
echo "Simfiles parsed and written to songs.json"
scp -r songs.json dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/songlist