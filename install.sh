sudo apt-get update
sudo apt-get install curl
sudo apt-get install unzip
sudo apt-get install sleuthkit
sudo apt-get install libregf-utils


### Hayabusa installation
Release_version=$(curl -s "https://api.github.com/repos/Yamato-Security/hayabusa/releases/latest" | grep "tag_name" | awk '{print  substr($2, 2, length($2)-3)}' )
r_v=$(echo $Release_version | cut -c 2- )
echo $r_v
curl -L "https://github.com/Yamato-Security/hayabusa/releases/download/$Release_version/hayabusa-$r_v-all-platforms.zip" --output hayabusa.zip

hayabusa_path=modules/evtx/modules/hayabusa/hayabusa
mkdir $hayabusa_path
unzip hayabusa.zip -d $hayabusa_path
rm hayabusa.zip
mv $hayabusa_path/hayabusa-$r_v-lin-musl $hayabusa_path/hayabusa
chmod +x $hayabusa_path/hayabusa


pip install prefetch_parser