
ceating conda environment:

```
conda create -p venv python==3.7 -y
```

```
conda activate venv
```
or
```
conda activate venv/
```

```
pip install -r requirements.txt
```

To add files to git
```
git add .
```

>Note:To ignore the file or folder from git we can write the name of file in.gitignore file
```
git status
```

To check all the versions maintained by git
```
git log
```

To create a version or/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```


BUILD DOCKER IMAGE

```
docker build -t <image_name>:<tagname> .
```
>Note: Image name for docker must be lowercase

To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image ID>
```
To check running container in docker
```
docker ps
```
To stop container
```
docker stop <container_id>
```


```
python setup.py install
```

Install ipynb kernel

```
pip install ipykernel
```










