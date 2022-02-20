FROM python

WORKDIR /home/zz188/cc/project2

COPY . .

# RUN pip install --no-cache-dir -r requirements-prod.txt

EXPOSE 5017

CMD ["python", "-m", "flask", "run", "--host=127.0.0.1"]