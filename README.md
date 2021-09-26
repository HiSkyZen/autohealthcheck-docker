# Auto Health Check Docker Image

[![Send mail](https://img.shields.io/badge/-hisky%40mchan.us-blue?style=flat-square&logo=gmail&logoColor=white&link=mailto:hisky@mchan.us)](mailto:hisky@mchan.us) [![Docker Image Version (tag latest semver)](https://img.shields.io/docker/v/hiskyzen/autohcs/latest?style=flat-square)](https://hub.docker.com/r/hiskyzen/autohcs) [![GitHub license](https://img.shields.io/github/license/hiskyzen/autohealthcheck-docker?style=flat-square)](https://github.com/HiSkyZen/autohealthcheck-docker/blob/main/LICENSE) <br>
파이썬용 학생 코로나 자가진단 라이브러리 HCSKR을 도커화시켰습니다. <br>

x86_64(64비트) 아키텍쳐와 ARMv8(aarch64) 아키텍쳐를 지원합니다.<br>
x86(32비트)와 ARMv6, ARMv7 아키텍쳐는 지원하지 않습니다.

보안성은 장담하지 못합니다. 매우 송구스럽습니다.

이 브랜치는 pip를 사용하지 않고 setup.py를 사용하여 HCSKR을 직접 설치합니다.

원본 리포지토리는 폭파되었으나 직접 설치 방식의 특성상 2021년 9월 26일 기준 정상 동작합니다.

## 사용법

환경변수 몇 개만 설정해주시고 다음 명령어로 컨테이너를 실행해주시면 자가진단을 하고 꺼집니다.<br>
NAME에는 이름, BIRTH에는 6자리 생년월일, REGION에는 지역이름, SCHOOL에는 학교이름, SCHOOL_LEVEL에는 학교종류, PASSWORD에는 비밀번호를 입력해주세요.

지역이름과 학교종류는 아래를 참고하여 입력하여 주세요.

```shell
docker run -d \
  --name autohcs \
  -e NAME="홍길동" \
  -e BIRTH="010101" \
  -e REGION="OO시교육청" \
  -e SCHOOL="OO고등학교" \
  -e SCHOOL_LEVEL="고등학교" \
  -e PASSWORD="0000" \
  hiskyzen/autohcs:latest
```

그 이후 시스템 크론으로 원하는 시각에 실행하도록 설정해주시면 됩니다.

예시) 주중 오전 6시에 실행

```shell
0 6 * * 1-5 docker start autohcs
```

<details><summary>▶️지원하는 모든 지역이름 보기</summary>
<p>
지원하는 지역 이름은 다음과 같습니다:

'서울', '서울시', '서울교육청', '서울시교육청', '서울특별시'</br>
'부산', '부산광역시', '부산시', '부산교육청', '부산광역시교육청'</br>
'대구', '대구광역시', '대구시', '대구교육청', '대구광역시교육청'</br>
'인천', '인천광역시', '인천시', '인천교육청', '인천광역시교육청'</br>
'광주', '광주광역시', '광주시', '광주교육청', '광주광역시교육청'</br>
'대전', '대전광역시', '대전시', '대전교육청', '대전광역시교육청'</br>
'울산', '울산광역시', '울산시', '울산교육청', '울산광역시교육청'</br>
'세종', '세종특별시', '세종시', '세종교육청', '세종특별자치시', '세종특별자치시교육청'</br>
'경기', '경기도', '경기교육청', '경기도교육청'</br>
'강원', '강원도', '강원교육청', '강원도교육청'</br>
'충북', '충청북도', '충북교육청', '충청북도교육청'</br>
'충남', '충청남도', '충남교육청', '충청남도교육청'</br>
'전북', '전라북도', '전북교육청', '전라북도교육청'</br>
'전남', '전라남도', '전남교육청', '전라남도교육청'</br>
'경북', '경상북도', '경북교육청', '경상북도교육청'</br>
'경남', '경상남도', '경남교육청', '경상남도교육청'</br>
'제주', '제주도', '제주특별자치시', '제주교육청', '제주도교육청', '제주특별자치시교육청', '제주특별자치도'

</p>
</details>

<details><summary>▶️지원하는 모든 학교종류 보기</summary>
<p>
지원하는 학교급 이름은 다음과 같습니다:

'유치원', '유','유치'</br>
'초등학교', '초','초등'</br>
'중학교', '중','중등'</br>
'고등학교', '고','고등'</br>
'특수학교', '특','특수','특별'

</p>
</details>
