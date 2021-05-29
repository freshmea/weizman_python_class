# 기상청 자료 다운로드 받는 방법
# 기상청 홈에서 기상자료를 클릭하고 기상자료개방포탈로 들어간다.
# 기후통계분석 란의 기온분석을 클릭하고 기간을 정하고 지역을 정한 다음 csv 포맺으로 다운로드 한다.
# csv 파일을 열어서 5번째 칸 까지 삭제를 한다.
# 파일 이름을 ta.csv 로 저장하고 코딩을 완료한 후에 실행 한다.

import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_list=fm.findSystemFonts()
path=font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)

f=open('ta.csv')
data = csv.reader(f)
next(data)
resulty2= []
resulty = []
resultx= []

for row in data:
    print(row)
    if row[-1] != '':
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '11':
            resulty.append(float(row[-1]))
            resulty2.append(float(row[-2]))
            resultx.append(str(row[0].split('-')[0])+'년')


plt.plot(resultx, resulty, 'hotpink', label='최고기온')
plt.plot(resultx, resulty2, 'blue', label='최저기온')
plt.legend()

plt.title('내 생일의 기온 변화 그래프')
plt.show()