# VSCode
VSCode는 code editor로 사용되며 그 외에도 다양한 기능들을 제공한다. 여기서는 code editor 외에 다양한 기능들을 어떻게 사용하는지 소개한다.

1. Installation
2. VSCode Extension 기능
3. ssh
4. ipython
5. git lense
6. better commant


# Installation
## for MacOS
그냥 가서 pkg 파일 다운 받고 실행 시키면 끝

# VSCode Extension
VSCode에는 아주 많은 Extension들이 존재한다.
VSCode 왼쪽에 블럭 모양의 아이콘이 있는데, 그 아이콘을 클릭하면 다양한 extension들이 보이고, 클릭 한번으로 간단하게 설치할 수 있다.

extension의 종류에는 python, c++, pddl과 같이 기본 language 도 있고, remote-ssh, gitLense와 같이 코딩하는 환경을 더 편하게 만들어주는 것들도 있다. 

지금부터는 내가 유용하게 사용하고 있는 extension 들에 대해 간단히 설명하도록 하겠다.

## Remote
    Remote - Containers
    Remote - SSH
    Remote - SSH: Editing Configurateion Files
위 3개의 extension을 모두 설치하면 VSCode 내부에서 원격 접속을 통해 코딩할 수 있다.

예를 들어, 연구동 1층에서 연구동 2층에 있는 서버 내부 파일에 접속하여 작업이 가능해진다.

## ipython
ipython juypter notebook을 vscode 내부에서 사용 할 수 있게 된다.

## gitLense
git 작업 상황을 잘 확인할 수 있게 해주는 extension. 아직 fully 사용 하고 있지는 못하지만 여기서 유용하게 사용 하는 것은 현재 git repository와 local git repository 사이에 차이점을 비교해주는 기능

## better comment
주석 처리를 할 때, 주석 처리 방식에 딸 한가지 색이 아닌 여러 가지 색으로 주석 처리가 된다.

    # 기존 python 주석
    #! 빨간색 주석
    #* 연두색 주석
    #- 파란색 주석