<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<h1 align="center">게시글 CRUD 및 연관게시글 연결 API</h2>

<br/>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

### Project Details

-   게시글을 작성하고 조회합니다.
-   게시글에는 연관게시글이 존재합니다.
-   연관게시글은 게시글과 단어가 두 개 이상 중복되는 게시글입니다.
-   전체 게시글중 60% 이상에서 등장하는 단어들은 연관게시글을 검색할때 참조되지 않습니다.

### Built With

-   <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
-   <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white"/>
-   <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/>
-   <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
-   <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

프로젝트를 실행하는 방법을 설명합니다.
다음 절차를 따르면 프로젝트가 실행됩니다.

### Prerequisites

이 프로젝트를 실행하기위해서는 Docker와 Dokcer compose가 필요합니다.

-   Linux
    ```sh
    sudo wget -qO- http://get.docker.com/ | sh
    sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    ```
-   Windows / Mac OS

    Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/youngjaekwon/KYJ_Board.git
    cd KYJ_Board/
    ```
2. Install NLTK Tokenizer
    ```sh
    pip install nltk
    python ./nltk_data/nltk_download.py
    ```
3. Start Docker Compose
    ```sh
    docker-compose up -d
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

### API Endpoints

#### /board/post/

-   GET
    -   게시글의 리스트를 가져옵니다.
    -   리스트는 게시글의 제목, 생성일자를 반환합니다.
    -   각 페이지에는 게시글이 10개씩 출력됩니다.
    -   Query Parameter
        -   page: 페이지 번호를 지정합니다
    -   Response
        - content: 전체 게시글의 갯수
        - next: 다음 페이지의 url
        - previous: 이전 페이지의 url
        - results: 게시글 리스트
          - id: 게시글 id
          - title: 제목
          - created_at: 생성일자
-   POST
    -   게시글을 생성합니다.
    -   Request Body
        - title
          - type: string
          - 제목을 저장하는 필드
        - content
          - type: string
          - 내용을 저장하는 필드

#### /board/post/<게시글 id>/
  
- GET
  - 게시글의 상세 정보를 가져옵니다.
  - 연관게시글 리스트도 함께 가져옵니다.
  - Response
    - id: 게시글 id
    - title: 게시글 제목
    - content: 게시글 내용
    - related_posts: 연관게시글 리스트
      - id: 연관게시글 id
      - title: 연관게시글 제목
      - created_at: 연관게시글 생성일자
    - created_at: 게시글 생성일자
- PATCH
  - 게시글의 내용을 수정합니다.
  - Request Body
    - title: 게시글의 제목을 수정합니다.
    - content: 게시글의 내용을 수정합니다.
- DELETE
  - 게시글을 삭제합니다.


<!-- ROADMAP -->

## Roadmap

-   [ ] 게시글의 생성, 조회, 수정, 삭제 기능
    -   [ ] Django와 DRF를 이용하여 구현
-   [ ] 연관게시글을 찾는 기능
    -   [ ] Celery를 이용하여 Background에서 정기적으로 연관게시글 업데이트
    -   [ ] Redis를 Celery Broker로 이용
    -   [ ] NLTK의 Tokenizer를 이용해 게시글의 단어를 분해해서 저장
    -   [ ] 전체 게시글의 40% 이하에서만 등장하는 단어들을 이용하여 연관게시글을 찾아 저장
    -   [ ] 연관게시글들은 연관된 단어들의 빈도로 평가됨
-   [ ] 배포
    -   [ ] Github action workflow로 Docker Image를 자동으로 생성
    -   [ ] Dockerhub의 Repository에 Image Push
    -   [ ] Docker compose로 컨테이너 관리
    -   [ ] Nginx, Gunicorn 사용
    -   [ ] PostgreSQL 사용


<p align="right">(<a href="#readme-top">back to top</a>)</p>
