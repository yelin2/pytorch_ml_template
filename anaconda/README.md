# Anaconda

Anaconda는 실험 환경을 설정하기 위해 사용되는 일종의 virtual environemnt이다. 

그렇기 때문에 하나의 local computer에서 다양한 version의 실험환경을 구축하기에 적합하다.

예를 들어, CARLA simulator를 실행시키기 위해서는 python 3.6을 사용해야 하고 pytorch를 사용하기 위해 python 3.9를 사용해야 한다고 해보자. 이 때, 각 필요에 맞는 2개의 anaconda environment를 생성해 놓고 필요할 때마다 environment를 activate 해서 사용하면 된다.

여기에서는 anaconda 설치 방법 및 사용 방법에 대해서 다뤄본다.
1. Installation
2. Conda Environment
3. Example

### TODO
1. cpu 용 env.yml 파일 update
2. gpu용 env.yml 파일 update
2. ubuntu, windows installation 하기


# Installation 

Available OS: Ubuntu(Linux), Windows, Mac 


## for MacOS
1. [이 링크](https://www.anaconda.com/products/individual#macos)에서 pkg file 다운로드
2. pkg file을 실행 시켜 설치 시작
3. Introduction, Read Me, License에 대한 동의
4. 최종적으로 ~/opt directory를 설치 경로로 설정 후 install 버튼 누르기 (default path가 ~/opt라 확인만 하고 넘어 갈 것)


## for Linux
need to update

## for Windows
need to update

# Anaconda Environment
## Create Environment
conda 실행 환경을 만들어 준다. 이 때 python version은 명시해주는 것이 좋다. python은 defualt로 최신 버전(현재 3.9)이 설치되기 때문에 나중에 다른 library들 때문에 환경을 다시 만들어줘야 하는 생기는 경우가 많기 때문이다.

    conda create -n [env name] python=3.6

## Environment Command

    # activate env
    conda activate [env name]

    # deactivate env
    conda deactivate [env name]

    # list of all conda environments
    conda env list

    # list of all pkgs in conda env (not a specific env)
    conda list

    # list of pkgs in a specific conda env
    conda list -n [env name]

    # remove conda specific env
    conda env remove -n env_name

## Install 
anaconda 특정 environment에서 package를 설치하고 싶을 때 사용하는 command이다. 대부분 conda install 뒤에 내가 설치하고 싶은 package 이름을 넣어주면 되지만, anaconda3를 사용하는 경우 가끔 명령어가 달라지는 경우가 생기기 때문에 구글링을 사용하는 것을 추천한다.

    conda activate [env name]
    conda install numpy

## Copy Environment
내가 작업 중인 환경을 다른 컴퓨터로 똑같이 옮기고 싶을 때 사용할 수 있다.

1. 먼저 내가 작업 중인 환경의 정보를 추출해내야 한다. 아래의 코드를 사용해 그 작업을 수행하고 결과는 .yml 파일에 저장된다.

        conda activate [env name]
        export > environment.yml

2. environment.yml을 다른 컴퓨터로 전송 후 아래 명령어를 수행하면, 새로운 컴퓨터에 내가 작업중이던 환경과 똑같은 이름을 가지고 같은 pkg들이 설치된 환경이 만들어 진다.

        conda env create -f environment.yml

이 과정은 굉장히 유용해서 많이 사용했던 방법이다. 하지만 최근에 사용했을 때는 env create를 하던 중 error가 났던 적이 있다. error code를 봤을 때 아마 gpu 관련 문제가 있었던 것 같은데 원인은 해결하지 못했다...

# Example
env.yml file은 기존 pytorch를 사용해 연구시 사용했던 conda environment 환경 파일이다. 환경을 요약하자면 다음과 같다. 




