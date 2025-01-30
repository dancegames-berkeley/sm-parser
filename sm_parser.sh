python3 -m venv .venv
source .venv/bin/activate
source .env
pip install -r requirements.txt
python3 ./sm_parser.py
if [ "$LOCAL" = "true" ]; then
    cp songs.json /home/remy/Desktop/proj/test/songs.json
    echo "Songs transferred to local directory"
else
    # scp songs.json dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/data/assets/songs.json
    aws s3 cp songs.json s3://dancegames
    echo "Songs transferred to AWS S3 bucket"
fi
python3 ./image_parser.py
if [ "$LOCAL" = "true" ]; then
    cp -rt banner /home/remy/Desktop/proj/test/banner
    echo "Banner images transferred to local directory"
else
    # scp -r banner dgab@apphost.ocf.berkeley.edu:/home/d/dg/dgab/data/assets/banner
    aws s3 cp banner s3://dancegames --recursive
    echo "Banner images transferred to AWS S3 bucket"
fi