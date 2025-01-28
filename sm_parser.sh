source .venv/bin/activate
python3 ./sm_parser.py
scp songs.json dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/songlist
echo "Songs transferred to OCF server"
python3 ./image_parser.py
scp -r banner dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/banner
echo "Banner images transferred to OCF server"