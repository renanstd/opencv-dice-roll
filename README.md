# opencv-dice-roll

Projeto com opencv, para estudo, que identifica o resultado de uma rolagem de dados.

![print](/images/print.png)

Feito seguindo [este](https://golsteyn.com/projects/dice/) ótimo tutorial

## Executando

- Para este teste, usei um celular Android com o aplicativo [Droid Cam](https://www.dev47apps.com/) instalado, para exportar as imagens da câmera para a rede local.
- Instalar dependências
  - `pipenv install`
- Acessar pasta `src`
  - `cd src`
- Executar o script `main.py`
  - `python main.py`

## Funções principais utilizadas:

- `cv2.SimpleBlobDetector_create(params)`: Detector de blobs do `cv2`, identifica e conta os pontinhos dos dados
- `cluster.DBSCAN(eps=40, min_samples=0)`: Identificador de clusters do `sklearn`, para identificar os múltiplos dados que podem ser rolados simultaneamente
