#!/usr/bin/env bash
cp -rf ../zoom-util/zoomutil/* ./myutil/
git pull origin master
git add --all
git commit -m 'update new version'
git push origin