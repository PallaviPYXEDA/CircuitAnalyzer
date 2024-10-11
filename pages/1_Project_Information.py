import streamlit as st

st.title('Know your ICs better')

st.header('About:')
st.markdown("Integrated circuit (IC) chips are vital for devices like phones and computers, acting as their 'brains.' To boost interest in the growing U.S. IC industry, I created the AI-powered app 'Know the ICs Better' This interactive chatbot helps users learn about ICs, identifying types, providing details, detecting defects, and making learning engaging with a Q&A section.")


img1 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFhUXFxobGRgYGSAdGRogGhodHiEdGx0gHSogIB4mHxcaITEhJSktLi4uHR8zODMtNygtLi0BCgoKDg0OGxAQGzImICYvMjItMy4vLS8vLSstMi0yLTAzKy8tMDAwLTIrLS0tLS0vLy0tMi8tLy0vLS0tLS8tLf/AABEIALcBEwMBEQACEQEDEQH/xAAbAAACAgMBAAAAAAAAAAAAAAAEBQIDAAEGB//EAEIQAAIBAgQEBAIIBAYBAgcAAAECEQMhAAQSMQUiQVETYXGBMpEGI0JSYqHB0RSx4fAVM3KCkvGiQ1MHJGNzk6PC/8QAGwEAAgMBAQEAAAAAAAAAAAAAAwQAAgUBBgf/xAA+EQABAgQEBAQGAQQABQMFAAABAhEAAyExBBJBUWFxgfAikaGxBRMywdHh8RQjQlIGM2JygqKywhVDktLi/9oADAMBAAIRAxEAPwBdwH6V+DUVlbSwN52a1x/LHolTpM5OResePOEn4dXzZWnfUM8d+1Vavh5lKXiI9yVmA2xUgCLHvOPEfEfjWNlKySg0vRTF1DmbeXKPVfDP+HsFNzTMS3zf8klsqS2gF7vUm9YF+mVU1cu1JlBq1wEpUQRIEglrm23XqcYcpcxc4YhZqLAafevmamPYYLDIzFvoSDmPRmH6pHk9fINSJRlKOpIZT08jj0UrEmYu7jk1YrPkShh84SxJcVoxgCpRB3GNUbiMXORQxgruiBJOgGQJsPMedzjglpz52rvHFJRMRk02i1M8+4YmLQfyGOKloIyt3rAhIZeY9gWH4gjKZpC7eKpqKUfULXYi0yRYGNrixvGF5onJk5JasrkDdg/K51eDSJGFmYkTCl8oJLtXhyFWb8mAslw2oi08zTeKniwqoZddAnXAlgB5jtvOLKxH9wylCjXNHJsNn70i6sMkyTNAYmwDkNqXv0qRfaOly3CW0VKjPVpV0DEhpAqAzIVrNJEkg7++EcTjkIWmRlBdq0LV1Fqc/wARXDYGYtBxAqnbg2/Hlq3GE1GtpG87bn8o/UR742ZM+amYK02uG56HzjGxeDkKlKIHi3sXOjagb0MWNRo1SRIWp+Gze42PvjSAlzlNT7vyjFzT8Ol6txt5wFX4NUXpqXuon5pv/wAcAVIP+NW2hlGNSaGh2P2P5gyhTIUFH0jY8xKGPx/ZPk43tjExs1Kj8tSX5fUOhv0PSPQ/BkTZahMQsp1r9B5sW82jpuD5WhMGowqkSEqhQbfdI5WHoT548xPM0l2GR6lLkDmLg824R7NeNmISyg6jawflp7xOnk2VmJtuGkWjr+2NL5EsgSwX1pePMH4hMUTNKW0rY/reKa+WDggCCPfoP7/XGxhcGoKGdYymlbvsN9Y85ivizg5JZzCtLZf9js5ZtGgbhuWFJ2PhUXLCPrUDARflmIv6C3XBcdhpiEEPTh33vF/hvxaWuaHoefb92i/I/Rkqut62oIJgADbqfP5Y8xNxeeb8mVLYktUk/iPcjHrTJC5q3AD2ueO/RqwDxTKqtF3Msmklj1BFoE79BP7Y0ZMuYlaRZQLAaEdPNvzGafiEuaFC6CKnUGtgeNH5wFnvoBX0LUVkqMRzBfh1RMIdiN1m11ONiVikLLD1pw9/cbxgLWZX1DyL8fNq+daRyuYyDp8Ske2GyCzxxE+Wv6T33tFT0x0xWCZonl8qXYKASSQABckmwAHfpGOKUEhzFkDOoJEeg5srkMqKSKTUJBJEGanl000xeTbVpiSSUy/+cvxGn2/e3N7AQ8kf5Acvz+/K7xwNVh9oifxsXb5C040ADp6BvWBqYX9S/oIIoZSo9kp1GtN4ppHf+zga5iEB1EDTcvHQCoskEtXYNFlPh5G7onlTXU3uTi5I2J5wIKOlOQginkKRJAU1DaGqPt3OldxgYM1gSQNwBfqY7MVLBIqXsTp0EG1qLITT1LTiAVVQoPW4PMZnoNvLFPkpYKUkua1dw/tERiiVHIQwoWZi3DXjEPCM/FJ/EIn0/v2wRJKQzUgUwJWXN40+VpWYBlqA3GnfzEWt53xxC15yFDw6F/Q9tFZqP7YyKrq/vBqqPjI2iFAibD85JH54X/uEFJ41dzfv2g7ykl01s9GDNGqTurhknUpkERCnyERA2EzhxKRLSCpXfe0ZcyaZyymWh+jxVltKLp8Ck0E3YHUZJN7+eHkqpQCMqaM6yStQ4AjTpD3M8PVqjNUWmjDSGWmulAY7bST+c4YwcuWh0qmZi+rO9aabehhfFYmasBSJeVLOGe29efqIbZRWpoVo1CgJuoYhSSBuAReI84wD4hhcLjZKgACQ4cXBGnGukUwfxLFYLEJK3YsWOoOtQWDasYEp8BzJcVXemIMhlZhb7xJkyOl/fHiZ0lMofLkgq0sAxGjR9WwX/EUpcrNPGVLOA4IIOtmt7wFnOHFiebUSZJHU9741cD8MnipDRgfFP+L8HN8Mp2HCA24K3ljeTgFtePOK/wCIUk0EV/4I1yfb++2BzsOuWQNNTbgADZyaNBJPxUTA71014knVgHLtAVfJNTJlTpJiehj/AL64UXJU5ChUehP3jZkfFEnKUmh6ZgKHi0VLlwWM8oA33kwelo2Hz9cDC1oCU33775wVa0TM8wU1AGv47pGjkpHl3G2G8hNqxnD4ilJZ2PlHQ5bjLlaS1V8YI+pRcAzFiV2FhaMYk74KxVMScqddhv28a+H/AOIkkCVldRYcTtpesQzVKk9J69TUMzUqyUT/ACaa3uOUCGsQJ9euG5AmOlCKpa5uej6a0p5QjicRKQVZ6EFmux4nj6+cc/Q4SzMFIUjUXNQWcj7u/wDK3njRk4Za5ruWa2nPnCGJ+JykyMqQHfr14cIfpQIxozcPMEtQlmp3NuW0YMrESs6DNFE7AV5719It/hVKlwrrUBvUVgOWIEiOa82YHptjz+IkibMEt6BxUEuoNrpTUER6DA46Zg5ZmNUsqhACUqfm9bBi2sLs3lnTlK8u/KpKd5ajOpT+KmfMjCgkH60l+L16LsRwUODxup+Jyln5ahlOxFH/AO3Q8Uni0W5Pi9SmJ1a6ektBbWNKwGNOpudOq6uJ88B/pULW5DKdnAYubOm2lCktwjs2flllIqGtcNqx/NYcwdZBKqdOvSWALLMWBMmTNhJgHG9JmSFSRKzOBQnXN0FDx0jxU6ViEzlYjIxPiALEBN6vo1ANekSWiX+AXEArNyTPwruR6SB5YYUPlp+vMH10HE8BqYRIExX05aaG50pxJAAEVmq20z5f9XwpNwcoD5iaQ/hfiOIcSplRq4r+/fSFvFKywaZBIs1SNypMJTA21VGt6T3GEJ615hlOjDgblROyRXm0eg+HSEAFaxUl76NYDd3AOohbw/i+boMfDaa9WpJpTqp01/EoMCTHYgKDM4un5YAaktIuf8j1vS+7tDE6UVklQ8Rs2g08jaOpyf0gyubZkqppZW0+IByMWJsDuJjraesGzcmdNlgNrob9fY+d3jDxeAS5UCzXI/GrXHB0v9ML+O/QtApqoeUKW1IJBABadI7gE8sbG2HUzpEwOfD3t6HjzEKomYuUsIIzOWHPn6h3cVehhR9CWorWZi66lT6tjHh6j+IkDUFkhTEzvbS2VjFqUlkjXrz5P3qPU4eQEJBKncVbThz3+8DfSSma7aizAbJJlSO7GBzE3MgbgCFCgTCqyuAPz5bbH7vBp6U5RWp8m577iBuHZQqmlUGuSddpPYAtYD0nBJhOfMo0s3d4EMmQJFw5JHdItypq1XbxQRpAsx5mnt0ixJIGLy5SUkS5Yu5oKcYWxOKZBnKPC9TtD3hnCg3MVqCmJLvTQN4YUTLajtG8dx3kNJwpzMqMWZ8TUW+XU3YvZ2LaP5XEc3mONUjWeaZqUQx0AtDR0JYXE72OOGWgKpb3h9ImmXVTK9v4grhmZDU2YMRrYqVceJoBHxK3e9hvY7TOAYlalKYCgqA/ffKGcLITLGdVzQkBqU0h5mMhTqrmTTAp0qScocxUcxpC2EyzAsPu2nrGaglK0uS5qdtO6U++mslSDQM7A+fdawDSphywTWCsQovbvqIkYbYSgn5igxuTQvswjLVMmTSvIjxAhho27njFn8PyknTa/iGS3oCb377YMjL8wMDtlow49l+EKTjNMkuQ13D14fcFm4xpKTpIB5SBqKm3lcecYk5WHnoBI8QJABvxpFMOjEYeYz+G5IszFi8azL6mJgD02w7Il5JYT7xlT5nzJhXZ9rRKrnGRXpCqrpWb4hct4Z3YHnW567x2x57Cy0mYmaAXTVtAVDyNNuse8+KZlyTLUANHo7A2fUAxLK56rTETIPr2I6GDY7HrFrYfnGXNIYMQXpSp1PHjzrGBIwq0JUFWUAC9aCwB0HCLk42yyNRGoQfMYvM/uKClJDi3OF5fwoSkKQhZAVQ8REU4v54cl4gpuIzpvwQ/4wbk+IBmAJA9Ti+I+JCXKJTfT89IHh/gsxcxlDw6/jrDF03I6dD++B4b42gsmbV9R+L/AL0i2I+CLS6pemh/O321gZqouCOkf33xq5JC8q3cByNQ51c13F2raMwmah0WJYHQsGowpoDZ3EK61CkJvBvtcfr8jGMyamV8xRUoN/i33jYkrxQlpCEH/qenlwbWsDeCV5lNu63X3G498VEpaaoMcOKlTfBNTXjfpFlOqv2gVPdOuOzJpMpaCGJHTrHMPKCMQhaS6QQToQH0PtB2TdWQBTMASPS3Ukx7nDWClo+Wn/YBu/4hP4jNX85ZLhJU475RLwINgP0v+vWd7YviJSVsgODuNIFh8QZbqLEbGrinfZgkJh5KWDQkVOYU8Q41Sp1BTMlpAtECelyL3wpNnpSvIKw/IwE2bL+YKCH+TyVWspIDMi36TJFt74ycdOw2AIWWSVkCr2F6DbyhrCS8TjwUVVkBIZvq5nfmTtHP16Omq6uDGtGYdxWBouP+QVj64UnSxn8B0p/7h9xG5hZylSUlYrru4oX6Qdwd25C1QxA1ByDSFSkDSdnVlNtK2KwQTPoRCXUWHHkFXbjoD2QYmYkICDrTd2qkctSNedj88+lBBIUnkFRdYRmCsCGjT4gABEbEXEyMEmS0rRMTMDFqMWKk0JDH/wDEkecI4ZcyXPlqlF0guXAISrxJq1SLqALaUgCtopAupLmwA6szGAo9TafU4GEf23IbaunH78Bxhozlzp+QF9VFmrq1fLiRsYVmRcuJl2L9NQtVqjyQfVJ5/PChTmq38aDmo1PCNdKmDCnf2EapZFnlECoFF1YkIkiyaV+N9MFtRiWwaThlzfEHNWcAEvqXNkiwaAz/AIhLw4yqNWJAdva5PGDMlwtU5nqCVBKjSEpC14ABhiJAYzv54fXIOH8afE4Z7nM9Bs0Y6sZ/WtKUMtXIFsrPXW7Rd/EVUV6RLpqXQ6q1yXYKQukkOTKiVhoYWFxjNmr8LUZ2fdqnpTdqCNnDYcFYWlyWKm2Bol6AgkGlHcmKcr9VT0KqCXKgQw0neXUI3LuCRdSFkEYc+Yg5AA5u9XYaUu504GM4yZpMxU1RSlgGJDEmlHIAYVNjUMaxaM4wJpinFOSRImbzBsO3YYsmRMWTMVL8SmerZRal9Pu0cmLky0BCJ4KUgsGfMb7jX2Du0adFOp1WABt/MnynDYSCn+4xIta416fuMwzClWWUSEm5rYigfjU31bSLHy60Gp+I5ps8wKg0hgN4kd/64piJKiAxq6ddql7eXvaC4WaFJUrK4yqo2poA9eLk6hqarfprm1pUhRQUvEqAeJUo1WcFB8KuLKGMzsewNowzOWQDx9u6ecW+GyQohSrCocVCmqOQvzMcMikkAXJwoS0bsd3wDh9NMoz1AKlBwNVakQtbL1ASvh1A32WMRt3BxlTllU4MKjQ2bcNw7cQ/KSUoIBZ9d+HQ9sYocctIMSzUyYJG081zuzRUkzJg/OoSSpTBknvoKd6FKgAHPi79e+e8rT6zvb2G/wC3z8sWxCx9I099PzzbjHMNJJJUdX8tdr25Pq0XVK8qyypNxBtHmD07fPFJQMoiZUC9NeBHrpYRTE5J7yaE2qLcQdGtrUm8R1TpQMRYTrMCYv7CY+fbDGHLEzVo1owc11/MZuOQCPkoW1KuaU0jYrVDcUwR5J/TGhmkyvAV+aoyDKnTTnCL7Jp7RIIYqvVpVKxCIus6lNGLAjp8MAarbDrjzsklkiUoJuWu/Z234CPf475S1ELdtwG3JpTf0jT5XLVGPgZo0SXaFriAqBJBZhYksIAA2PkZZMyagf3Zb0umr9PfjzEJIkJIaUoHnQ+vf2T52lmct4figMKya1ghpU/+S3tDDv2wygSZv0uMp5fowPNMQ6SLhrP/ABv1vGPmJgxeOv8ATFkUonvzg0zDuyph04acoYcJ481JXouuqjVYGooADlbSqk7A6QPdr3wticEZpC0HxCztd3d2ce1qRaTPlIcEdQbUazsfSCa3GEJdqQNNCRFIknSIAt5EiYFgDHTFZeHUgJzfUBcXJ5keprCk4CapQH0kihFANSwPoC13gZs3qHUHrJ697dMMKmTVqCFHw6NoIWThJGHSZgHi1O54bP8AzFlOmCYGo2nYL3tc+RxPmJQKioNavToL2pApktaz4SwIDUuTzNqEAjVt4EpVyjQDeAZBH5iZF7QcHlzizinfrC2IwSDRQcd+UG0c0Jk8p+8ot7r+2G0TUqooRjTsHMl1QXA8xyMMsrXhi7bH7SmUk9Y3U3v6YIiUETBNlgUFrPSlf0YWXPMyUZEwmpF2cB3PN+Yg6mBuCCT2Pn/18hh7CqKnz/U54U71jPxKcrZQWYcatZ2HGnOJ4bEKwl+i30MatnfEriaNOWYyCCZME9ZO8dx88Scg4YGZN6cT3WPUJxX9WhOGw1CWB/6U68OA5+XrVOpr2OhAINrKAOlrmP7OPBzcPMxGKVMxCvCBmPJ6Dg5f12j1rS8LKRIkJ8Ron8ngB+LmPKPpNTcZhkbdi9OSbxVEqT+IMq+5ON2RjRMkhaQwAoP+0/h4VHw1MpShmJdTvzHs7RDJ5qQ7AXOirpg28RdLiwJs9MmfxYcMxknKMzOCPUe8ZkzDAzEhashLEG9R+vaCG4szsFRSqwQrPAbUw5iAFgpAMa4aWHaMBxOKmEKBLJpQf4pGj3cm7OA19YfwXwuTLyKIzLDkl/qUdeQDs+7NCipmixB1BVTUFYdItUq/7R9WnmZ64ibkOS7U52HW54QRaEs4SB9667t7xNXNgFGqUAToGAmlTP4aY+sfzPtgsvxFn3r/AO4/YQrNZCcx72HMw84fkzIoqdp1E7sxuSfMzJ9RjQxGKTJw4XLUyQ1QL8K8PWPPyJCp+KUJyXWXoSwAFNONm0BMFZ3KsDsYFu8f0wE4uVNwpQkDNdmyvXR+II5g6QSXhpkvFhaictnfMR4RduBHIEawOiqtMoyA0io0qQGQEWJANgw5YIvbF0/InrSoqDAV3D7bPTnEBxeFBCQQoqvoWJLndq6sDFAWBKoWOk78u0mBqIufTFZCU4VZWlJZ2GvEEsHFND7mD4qYvHJEuZMTQBRNuBF2LHUHfQGLaSyVGk6mtEyZkggAWN4v2nGhh5sxahOUrwmwA00fV4ycUmXKBkpTVJqX11bTL62rFfCtLVX1kLTRC9QNU8PUADK6WUGUIE2mbbEYXkTkzZpJFnYs9Kd9IdxWDmS5KMpPiajh81fPYXqQ144b6ScYbNV2qnVp2pqzFiqDYSbz1PmcdWvMXjWw0gSZeUde+Foq4Tw1sxUWmtREZyVQu0KWImCYMTtPcrO+F5s0S05i7cNIbly85YDvu0F8L4cUzGjNLWoWI1opD02iVcrElQYnTBINjgc6ZmluhlD3HtBJUtlXIOnA+/4jpeNZxnc6/BNQE661Ek0656OQbA3IsIJ1GTOEEJSAynY73HDusOB6GWQ4007O0AGrKCnGzSApJALQCY+EEwL+QxdOWWrPmpx/N44sTJqcpSAdx+ItoAyEUBT3Y/3fFJgNZqqjYDvrFpcxKWlJLK33PdollqR1xctuBFh5/rvgiylaM2am8LAlCynLVraxBGmRA0ncncAXMHp5nGgJYlgLdm8jzEYKpypqihnzEcxyMLm4pmmJOXVvBkhJWZAtPuQTHTbCapGHUc08DPrzjZQtcsZJROUWrDPOECmrJAJU+I1Jyy3sqOkDwyIsDawjbCqEOPlq3o7A3LkGr771c3jXXiCmZ80baVS7UDabcG1hTUWSBAuBYf364dlOkEkuB9oTxCwpSQhLKN60c9aa7NbRzamWExcqJudrfpfA1TWQVEeLbnbrBkhSpgAJy2flfkA97ecM+HZJNVI+KgcuVZKiQixsXJsyx9mQemKTVKyKazO76cNjsYGFhSw44MN9y+m/CN57hZGnllNAYMJYMslBVJI5BUKkrMCDaQJxeXO8JKr7GjPpxIHXdoUmS1GYkJ5cyL8g/SF4yoB6+mHJCUTk5xaEsXjJ2GWZJYkaiCEGgE6Ry8xMEm1wOvr8sBxCUv4X24V16RbCTZqyBMId81bsNKbwvpO2okzrZ9UNJZZvvtBnpvAtgaEAhk1ADUsdLXcdmHZy2LqpV+I2rtBlRDPOpvBNtMjsYiVtsZGCy2oaFurNCE4s4SSH++v3eD2opWuhSk5JkEEUmksxJA/y1UBVCoGJkT5QgpD1PvQF+ZJYAUAgAmpJyqpttUgAcGDkklzAtSqUZdD6Sd5DHoLEKpuZt6H3IiapCvCDptr101gCsNLnS3W2vp+YNyOfIqaCoWbFgSF1TpgqQD2uIthuTi5ZKZmWp12BrXhvCOJ+HzEpVLzux+ndqU48CIZpm4SaoNMl2VQwMVNJgsjAQRMCDBv1w2j4gggKNjXpvvCK/hk0KKUl2bd3OlmferUhjT4jVo5c1FgUy+ksYKlisKrqbkBirWgz1F8L4+Th8WuW8wg6NZrng9L6Q58Mm4jCmYUodr6EMd9ReljDqhxIjLqZ1PUMlQZUEmFRQfhHKGMk3gzjyXxvATUFMmVVCqk7kctnYelXf1Pwb4hJnqmTpxAWkMxP0p1uzOQX9TZuP+k1Aurjn/iE1a10jQCml0KuCQ02/OY2I8IgYcJST4SfehpGzNmGb4k6D2qITZWqA6aQTrqaBBA5cxpqKxmwAcMLxae2NCQrKo5i1K80eEjyYxmfEJfzkMka0/8AKo9XEW8drUlZqdKoCV1K7qbqF+M+R+yPMz0wOWqZMdSxQkMCKH/WuoNzwpDaZSZaUpcO1SDUNckaHQDeF6A7AAGVAU7BgJRD+FF5289u2LUu+9eH+R5qPhTwiTNm6ew6Cp4ww4fQsKguYPh6vuk8zt51Gv6R3wygKLy9VXbTYDkKc3jIxakJaao+FJezvDIuaJbxRpEyQo1q0c60yFZWANRUJZSTAggCZ6JvzJZShQURo45a0a73eApw4ROC1yygK1IOvKxZmFGjOCcZqOzahrGqCQwKA2OhWgSBI3k9CbThJGEBITmy0oCP8ag00cOKWckCsaOPxKZcvMlAU5HDxOGrYgFiXuwc0i3N5xBWZWJgRMXhmIUKIubkWA6iSJEtJ8X0PmUw8rtewsLO7WYZhlKTLdYBQly1Kg2e1Cak3y3d4ll8wtVOR/DqkVE05hdMFZ1Mi3aUUwBDMzstl0th2ZiFkZdKO1z5amw4PwhaTgZctWZQdt/pAuBVqD6ieW5iOa8Q0iKdM02IOhPiZW0HSur7V5vAmxjFpOZQzE+Iijf6PQjbUQtiBKRNCW/tg+In/f8AyB9CRZiRC3iFHwcguWqBTJ5nRB4uqdbAn4tKlisneD2GH0mWE5VvWxFjAk/MXPM1DUZwaNcC4fjtVqtHHNw8n4GVxaSLaZ+8DcYAtASkqBcDu0bEmd8xQQQyjbjyMdhwzKJSpvTYI6rC5rKV5p1QBUGirRYCdRDz3g9QRGNMUpawRQmqSKgjUHvjvGvLSlKC9R5EK/HbvAoqOFk6nmBc6gQoAAJMmwAjyHbEKZSpmUMCODHpo14tmmol5iCoE8x11eInm0lZmII6e3zwQH5ebM2/8xQvMyZXoGb8RM07mSVUSCWsPeTAxzN/acgE7CKkf3mSogbxW+dy5YQXqEDmFJdRnpBFvmcESZkqWyQBs5amr6vCsySmdNzKJ4s1+DaRX/FusgIqMdjUcl46xTpyfzxZU3OQQaDQCnCpgSMGlAOa51evKkVVkYiKjtDbA6aKGfskXqH5Y58wqLj/APb9QRMpEsMkfb9xL6/anVdEAACpQcqABFiVk7bnfFWl/wCSQTuVCLOexF3EmYHW4CGpLHSoBv3AAYUzMgbdRO+AolCZQeJqVf8ALZtCehFY1vnmUzeF9muPVuHrAOX1F+WJYgDaCTAv277nr2wypKUIJWaCvJoVExU5YEsMqrnd++PlDehXpeBpKQ7SoqBRHLcGbG8ifiBUyIthM51TSoFwKsb8mrZi1mNN4NkShCQaFVH+5OxodXFYsrVtdDXUSq1VnAFZydOlUH1d92vfVcYYkp8YyMEsXGpLs/LiIz8UvKCCcxox0Gvnw63guq7ZdmoPVDU2ClwhDIxVQVU6hzKCACBbfriyChaStIYgltn1LDVtWd/OF5iJ6VhBqCA51AqyXNg+j2MKqraiSLSegMSTsB84HQDHQonwklh58/zBPliSnNlBWfIcOQsIx6QAAZWn8ZAF9oAvgksD6gQUm0AnzlnwVCxfKPuRSL8tSJuA0ddACj/k2DlRAyJLKNtBSECEk55gdIIdyVGtqCgjVVb9D5aix95tPoRjpSkWbi28B+Yu5B4OAKbb+cQ8P2/l8+nvjpQ9ooJzUPffCMan7H07iP1wFcujGGZU+uYGHnDc/lnSlRzNLQtMEs9NSzVmiBzbrYloNtQUSQCCrME0TCpNmYAMK7kGh0A62htAlGXlepUCSpyw1AaoJ39C8IF1LSdAoDOxJIZpZLHSROmZVTPS4G84aKVTJaUuzV4P+BVoomdLk4gzCMwIaul9QNRfl5aOReBEEKup21Fqal1OlJKSrnnW+oTp21YOt0jxVA/mnekAQtMxXhoVGgbQUqHrVq0oTtDbIcSeiQzIssnw1RqRkP3QTEiBFjbUDuMLfNJ8JdmbYpcUtFzg0B1IYkF6MQog1FfLzrDDK0lSk6ZacyxCFag5bljNLRABvPM14YdVjDAwrIUoaVcspw3pS7cYSm41K5yEzbqoyXTlL058HfS0c9xDg9WnS8HMUylQ0mW3XwX109F4IK6xI+6R0wCV8qY0xFR2D1tGkudMlrKSdvI/YGKBlETUVnmNSrzqVJ01AF1KbhUDhyNzaMUMnOlJOwFDvfro8GGNUiYpI3+zjzMWnJrrFJjAZqiSdyEhmEj7dViDO2nzxRMjKQpnrYeQ6JHrF5mOUuWpiAwueNT5wRnmNk1BWLiTsFKkQZ7KbeoPbDicMJXi17/jzjH/AK9c4MfpbzB/N+TRPLrVWoFqUi7Wc1EYcyoWao7ggq5K21GCAoAA6o4oSwAQB61OgpatTwG0bfw9apuZOY+4AoCa8GA4nWNNVFSdNMKtQ0yabaoEteYJYcpO1wEtEDCMqbMQoBZBYmrU/h/fWNTEYWSUlSARSla+uv4rEq6ik6VQjc7FjUVxFAJVYipSDXhkDBRWO8TsBhyVMYEahrXLiopQaWcs+pjOmyQu9qitqavc24AnhDCmz1vDqVKShp1I5E1QsEBGMRJ1O7GxLmemGZCUomJdYFfEPIBurAddTGTjZ5VKmJShSgfpNGo5JLcieg0aC6GadHWoPiUmCVmeU9Ovlg+M+ZLzozUJADGqQRSjUc/mE8KmXNyLy+IJJ8QooguS76C/lEGZdGkAtWaoWd7sYg8qiZliSxYifi8oYw5MooKiEpGlzWw4G9oBOUmbnoVrOtgwqVcRQMGp7rzlkZp0yYI72O43tO14w/PnS2KhcDukKSlTKJe55V3fhejxLjnG6bFBVqUi6AqugAuAYGmVWYsIXpjFXh5CyVBJAJdtOfZjbwuJx6AEoL8SLcHLeYBhLVzAAlaLAffqsKa/+Ut8gMKrloUqivKvt+Y2ZE6elLLbp39opIqtfXEf+0kDy+tqkD5YH8tApd9z/wDFP3hj+pPLl+TFKZJWOqPFN+Y6q0jrzHTTB9zixzpDOw4Mn8kxz5qSXZ+bn9Rat+UNqi0Al4J6NTogLFurYp8tqt9v/Upz5COma4bvyEaqVVpiGIpj7pcU/cJRljPYt++LhBUXv0f1VT0gRUIll1cyaVKoZ3KoKCNPXW01D7HDCZClFv2fK0KTcZJlh1Ki7/Cq5+zl/wDcajN7sd8MjBLbX0EIn4xIej99Y0c3oqtVLa20k0lA0BYMLqUQabEDXCmAWEg3xlplmZLyAMHq9X5GrgWrs1I9KuZ8uY6qlqNRuY0f72ijJZpfEHigPTFQVGSdOom8FgPIfmOuLzpBAeXdm3Yef55QSRiUsUrpq4u/fLm1IY5bPsAiVFFSnTZylJ9gXG5Iu0b3PynA5UgEFSaEj6hwOg0tawgGPxOaYAqrGo1Iajmoat7nWCKWdSmKOhjV0KxKONVNHaZ0i4PQydzfyBJgUoL0oADr29oTlpSFozHUkj0HG19rPeFvhTc3Jjz9LSOl/SMclPaDz5gTXvvaLadO0nl7Xue+mAANrm+LzCEKAudW05wshXzUmjPYkX/jjGlaDsAe+5+Zx35yrIpyipwks1mkq5mnkGEEU6Dv0ZvXb88GEqasZlUG5/cKLxOGkHIhuQrbgIqzNGqpGqhUCFtCuFlGbtIm/r2PY4spHySyiPOBIWMSjNLrEqb+/n/XBEqaEpkrpFgH/X9P2+WDZgYWKSg1774+cWZeiCdyPILqnyEfrimVLhxQ+kEE1eVTM4Hnv5CrwQ+QYiyP6kib/h/rhmdKRKS5p3tC0qdMmqLF+TtTjAdXKyDIkA38j59sDKSkse2gqJv+Se3jedbWTVhjUZ11WU0yCwmVtAtsOk+uF5khC1O1L9YfwuPnSkfLBFiOjW58YjX+kz03GYUgPVqyAE0AIjadWkbF4gzvFTvi3yEKkFCg2bjbl9oniVic1/ltX/Y7HvUR0H/xfqQmTzNNoY61kdQyqw9dj88ZXwUqEhSF3Brzq/tGjiwkzgLul/I0/wDdHnycWLaQ+wkHzVkKkR52+WG1YZSQch7d4PLnoJ/uJ1uOUHUc83I27B6TEj7wplahnaNEbfaGBpmrlrrx8np6+kXm4KXOlEJqCAD7mG3+LJVpwzqwl2pqyklU8Mv4a6BrV2qkwW5QGHxTpw8cTcM7cN6UNqaxhJ+Fq8JJKaZXcNRyCU7F9A7va8bKUxQ1IatNWkt4oCArbShMwwJJm4HcXtk4qXOXMzpDgUHDc89OEei+GT8Nh5ZkrUPmGp6WHAa1ueECGqGsG1mSD4alrgwZIEAWtJ2AxSSkprkI2dhTu7Q3OmJUwzjo/wCI1/HsrAKgL/daqq1D6ATeO7dMGSpxW3AFvOntCc2Sm4NeY9q+8GZPilKGJqimy7pU5HE+Rt1+zbD8uaUkAB6Xv+Y87iMAtQJ42Gr63HIuY3/jCsPq0qVR3VYT/k8L7gYuuexdV+P4r9okv4ZMIqQB587N7mBv8SrPZDTQbQmquwPnHIvvgSpoKsxFdzSgtesOIwCUJCSokAks7VNLDcXrANanqMVGeoequ8kdopUZt6kYhmKVV++Zg8uTLlUQkDvziceHy2Qm0DTSDdyAuqrPlbA2fj6/gQV42OXnjT+MgU5A2DPVLVD6gYqoPT0v6CkXSYrSqHPIGqNO9NDVZSd/ravKB6L++LJlKa1ONPQfmKTJ0tH1qEG/4TXqAFkpqJ/9ZzVa2xCCEBwxIwa1qKQ4bg1+NzCGI+LSJSQU+J3tw328oJqcGGkeJWrVYHMqjQg7yqdPfHJkpOHzZgM3+Id36m0DTjZuJKfleFNMxIsduPlF+XySU5NKmqgfaAv7mNXsZxVMxzQOWdoFOQVJ/uzKEsKUcd8IKWuYg7Ht1j+ftPoMOScVLK85HiZn4RnT8LOly8r+F34Pv/PnEGzVMGC6g+owZfxCSksfYxyV8MxMxAWlNDxEcd47W18w6H+v74yBKSn6Kd7R7szCv668/wA/mCaFJ30Kikl3CqfMmAL239t8cKklRD1ao+8DZSEZ1Cj3+20MKWTWkT45D1KVbS+VS7spE6hUuoF5he0SpNgpmZgnJ9JBrsRTavmY5NSVFT0II2q7Esx25RGpVDEgJpTUSqltRibBvQRJPbHSFGpNWYwMCXLfLZ6d7n03jdRCwifi67EA7n1O/pGBFQRbTsD8wRAKiSe9/LSJ0qYFgIA2Aj9AJO1+uKDMshIqT32I6tSUArNAPbvWHXCckpYAlVJBliJ9h+mPSysEiXLSP8hXrx4R4jG/EpkxSlf4mjcOW/8ADtDTiGQamQs0wWWVbVy9RqaLgWPTFJGIWsTGdgS7h+TVZg1m2i+IwyZZlZm8QH0nTVwRdThi9KiEXDeKmpUq0dGVDU0KLTZ2qLXrFiNVENK6jttuRcaicZ62nJM2viAAoHAdz53Mbvyf6YplpahJUSS1izs5pQAcKROtwOnrK5UsjFgiZapdnC2eoj2QKIa8tOg9WCjqSVlxUGtNE6E89PeAr+j+5QgVdqq/1DBqdDwgWtlmQlXUqwJBB8iQYIkESDcEjFUzAQ4MDVKYsY1TqQQbn0JB+YwUKJSxhYywFOBB9KuukrTOljMB2YqS1jqBBU8sKIg798MzEicSEnz+zVFW8oDKnfICTMBLf6tfRwaWfTXkw+TpukN+Ehk1tBAMkhoIDwAoVwRz7iJwKXKmoWVqL6gPUDVhrDOIn4aegS0pAsHZnNWdjzLizWaBv4kOGEKKJVi3RguxEfeuAPMjtgeHmTJkwoVYVNCKQXFYWVJlJmIJzGiQ4LkfbUvpCtKaVRVzdZZpg6KaSRqaIC2vpRbmN/nh05SCs20hd1y1Iw0o+K6jdhqeZNopzPGsxUUK1VtKiFUWAERA6x64XByghIYFyW3N/OHBhpeYLIc7kuaW5dIU1suDtY+W3yxRmtDgmf7CBy1Sn6HtsccIB+oQVO6DBFPPKwhpHLpkfdudInYSfMR6CAGQUl0bvXffvzhj52akwcKbQzoVQQLawogTNSO2lqhFNe9hgOYpoaeQ9A5jpkhVU173pBtOvrtOsbX1VQR1lV0UVPqT+uLdG9PdzACkiLQ2oFASQBdPqnCjs1FAOUW+Fi2JavrX3P4irRnnJ0iYcNSZUveHq86+akGOmKtVvyH6CkWBjGOu8eJ12aqPIq9TTSHsDjoGXh6fkxwl4oq5tSdJcMdtMtWJ7g06emmD8/ffF0y1Gw+3qXMcKwkOSw4wRSytdxCUnC9PFYUlHYeHThiPXDUvCTVXH39TGdO+KYVH+T8q+tvWGOR+jNQ2NXSsXTLIE2F+YycMrwBCCp66O5hAfHUmYE5Ka1r+PWCk+jdGmdRoyxvqqczHzkkj5YNh04dafDfazcxCOKxWMBaYqmjWPIi4g2na156Rtv6fljqZcxD51DLVw2mleAd4F8yWSPlJIX4WLvUO+mpZtmg1hYsxEgGT/P8AbGatQQQUhmqBVgdA1rVUw1NXBjWQnOkhRd6EhnIepfnRLlqBwyhC6lSkmTCzzA3nsCOumZ9Tg2Rc5RAS6t9BYGrGoBoNTCgmiUkHMybNqQHLkOKKUGfQQTVygZZIAgyOn5+mKTCVTlIklzQAnQjVtRvXjaDoSEyUqnWDkgUcHTgbN5XrAVRUJ2hjeOhAMGYvN+38sUXOK1kKl1S1Bc18masXTI+TLSUTWSp6mwoG6u4NngaplBJ+uqC+wKR/5Uyfzw0rCrBZKktxFfeFpeLkqSCuWX1YkDyjj1X2B+0BK/7l6YQUWDx7IDMWi8Ugb6Vj05Z7jVA/I4GlwKmvR/SOrU5LCnVov1jq0/M/sPyOIA1hAlEmLkUnZTHmbfIQPywRMmauwhSZisPL+pXl+ovAPX4jvHQf1wvOR8kZHqbwSRN/qFCYzJFue/Sw6wdk6X2vl+p/TGh8KwjAzldPzGV8ZxzkSE9fxEq+aZSG8MtSizUzLL3JUbjzE+mHJToDs43Gp1LcYy5qRMOXMyhoqzaJBOwpVucO8nlS9EVabJUTSWOlhqVRclhNup6HyxJ2KlYeW1gTfLSt7bjXeKSsJPxE0puoCgKq0oL6AtTaxjnnzSlFy9WmlWgzNoAAFRS7ElkI+J9LEKDsSSdgMZRUCrMXp7Av0ejnaPRoQpKS1zfmzDoKkDeJqQaTKtepUyulS6skVaZB+qy4qMwfTcCQAB0jWYiiWr5g0KiCLbDjtFgAVDKPFsQ5SgEEmmp4HWAcvnarmKwLoGD+CCVUmBTVVcEMEUR8MkkMAIBxJoQohZvWvMCrCmgZ/OsdkD5IKUG7Xq7E6nUkl+lIupZcqYLzzEEkRFgRAJ1Hci4EEYqhBBYnSB4ifLWnMEi7d9ItqMBdREQNUSb9z0k4OFAKFYQKCUEM414RulWgzcz1BIPr5n1wzLWQbVhKZKSwrTb+YF407VqqZOiZYn6xoG4k80dEEz5z5YOQwEpN9YthymWhWLm2bwjhYNxNO3hbxrNozLSpf5NIaU/F95z5sb/LAZqgSwsIewUlSEmZM+tVTw2HQQuwKHYw4kSMxIgLWgatkwbixxVtoMmb/tA0OhB7GRaR+eOEAhjBRukwwyvEwYD3ggybixBFjYbRYbYVmYb/AE8raNf8wwnEf7jr39oZZB8uylfDXeQy8tRD3B7dlNsDUuYlQzGm2hiplBQJlmp9IO/hjOrx1PZ/ABrgdix5feSTjqZqLMeT0gK5c0CwiPgUmZfELOC4XxK7MaSkyb6QEWFDGL2Ha+GEKaoAEJrlzVUz9EhqdXPtDOsSgQx/DMU1IEAahULEaQSh5IUNuGEsDMQAv/VmWGScyk3s/PY8oN/9Kl4hRVMT4VWNS3DcRflOKyPrFg91uv7/AN9MaeH+KE0mCMXGfATLcyFPwND5/wAR0HBa0kwQVIg38+h2mf2xpzFhSApNYwCgJJRMDaHRvxXto6/guUoOjUX+NrjVG3dTtI69ceS+JYpap+YFgKbF9ePLh1j1vwXCS0YbIsOVV0II0ZqFtePSOV+kfBq2WYOg1IbAiTB8wRa3cm/fF8NjMRiPBKVm1IID+eodjo9jB5mCwMh1zk5NApJLV1Y/SbjVrhzCTM8SeFBQ2ImB8h7RPyxeUuclZ+Ylm99+Z/OkdxGDws2WBImgv7bCxYWsOTh4zL8QVQJBI2kd+tt774YTjQsANlKRQHc0JzWtal4UV8ImIUW8SVKqRsKgZdgWetQIJzPFEiAQR1/aBjsnFSkIzg+LT93FbcrM9Kzvh+JXM+WR4dSfRrFxfiWCnavOUArVBUrqVKsW30nTHLT5SWaDc2iZjuRoVmWTnoRzru0PT0GVJCJaHqzWpzg1uIUgbU7f6V/U41f6zDigT6Rgj4VjCHKvUxy60SrHSzKD849t8ZqUiakOxb0Mepm4kyVEEEPbiO+kG8S4Y+XbTWUgwtzJQatgzJOmY2mevbEStBSbuHDcRzgWactQAICSxe9DBHB8wAzhqKtqpjTOpfDLTDSILxYxa1uuKyhMWMqXd7htL7gXsY5jBIQc6zRrEu72brqBDPPVlCimrLURbrU8PQ7agCQxkkwZHT0sMNBRl5py+QD0PHn9ucZZlpmZcOgbKUf9afSOA9SYCy9Ms0fM4SkSDiJrecaOKxKcLJccgIYVtURTCluisYBANxPeMeimpISJcsfxHlZSk5iuaTzFa79Io4Rl1arFNv4WqOY0an+XUuLASAZ7oQcLghLlLpO2kGXmKR8wCYm2YXHPXoQeEEfSfMg1ly70FpZkGarUqkrUpsshdK2IaRIqQbAXmMY/zFYiZ8xB8OgIse9nj0kjDjAYYoV9Va2p+qjlFjZZdIUgagZ1blTFtPb1/fDM9IleAHSvOMnDTFz1fONnpeopfqOdeAhbmyKaAvIVSIaCSD0uBPkL7QNsLhCh4mv5GNETELVkCnI8xaB+Ho+YOuiusBhTCHRLtBc2k1NJuxKwN+xxf5TUOpPSnlQUDx1S8oL6Cuuu3E7VvFmWJCVh4VNHVXs5fWCpXlVQtnJDCCoFj3k2H0X9rP28BWlPzUg9bs7HsPwrFgBMFQTYEGIs1puLTPWMUBCgx8oqUGUsnbWNZ3MGhS1sRqKr4a6g0H4pMEwUsT+LTOHkS0p/uKv94QdU5fyU/Try2/8AL2eAFH8Nl5J+vzKyT1Skfzlzf0xcnInifaLJH9ViP+iWehX+E+8JhheNWMxIkZiRIzEiRmJEjMciAkVEU/4erkwdJgnyMYFOmfKTmvD2DQcRMEpwCX9Kwv1FTHUE+3ocXBChwMRcsoURYiHXDnNVWmqwCgFgAu17kxtMAg9xvOEcQEySMiannfv2vDeHCpwPzDQcrd/xDfhfEEy6gGaVSAFZIqUiz65Z0KkhyhNPkEgdpginLXNSQgONXoWDOx51uIiJCZawZh4hq107YwXRyTkEnSiyCwEqgJtOkmxPe+JKlpcBT2LG5YcYVxOLIfJoQ4sxNP59Y2dIIXUAxnTNg0GCVPa9pAnpIvgieXPg8UJLPflFmS4jVy7lqZgkQynZhvDDrhyRNKOUZmMwyZ6b+XfpDvJ/SoFSCWov95ZdfUAmQe24v0wecqXNR4khStHanXbh7xlyMJMkTRlUUp1Z6sNq14+0X1PpLmatJVzGjSCSGDDm7SZgkC0gDrbFsJhZOEUZgAD90imNxMzFhMlJJy7ivWmn87wnznExDAlpOxQAER5keZvffCXxGeuatktlpcaiNj4N8PRKSJiqLrroRClsyOigeRJj2E29JOM81oTHoEoIqIqNY949LfyxXIIvmVrGqSkmB/Mfrvi4JiigIlB7j8/2w0JK2hBWJlAxGtRAcgVEqICxFRbKQttcmOixJvaMdlLSlB/xrV3PTq9G3iYlK1zAS6qUAIFG+zVfaHjxpenl6jtS3qU2gNKLJYqv2AFAmd16xOHUZAoKWxAcpI4sK8S8YqjMKSEuFEAKdqs5YcBc61hfMjy3/l+/ynDvzEqcIr3b1hMS1JIKg23rUb2PWKySW5jJuew39PL2xiKKinIzAabbx6NIlpOcEkm5Ou0M8umkeZuf78pxu4SQMPKfUx5jG4g4mdwFB33tFwWfiHoy/l/f88MVP1DqIRJb6T0MP85SWnQKsmXzdO40ltJLkEi8ao5YncX2xl41UycoSZbgnXgO/ato1fhaZckqxU1sqXFLklmuKj2rS8cb9G8jUTVWrCHJ0qNza0lpJO3UnbFUy0S5ZUsPoB+vxDeKxKsRNTLlHZROwuL+0OkUk363JwHCyTOmNoLxXFzhhpVL2Ec7xziSNUhmdESRSZQYNQGC4INwm0dZOC4mb85eVH0j2/fsOMG+H4VWGlZ1Dxqqe99efKEBo1qJFam5gbVabG09yLr5g/niqVi1ocUkLDGsdHwz6TLVREzNRA1PlQsmldHKT9YskVGKQSViDO5OOmWkl27Gg04aQtMC0ghOpfepo+5YVFCXvF9YLrVV1LZy5cg6YbpAFghuTcx54iEqzhA68LufaFZhQZSpj8gNXZhzd4XZYLmazVqgjK5cXH3r8qertc+/cYbcKU/+IgKs2HlCUj/mLPlueQFoXcQzjVqjVXN2M+Q7AeQFsAWoqLmNCRITJliWmwgfFYNGYkSMxIkZiRIzEiRmJEi7JIWqKF3n/vC2LUlMlRXZoe+GS5kzFyxKu4PQX6NC/juV8OsyyDYG3n/SD74FgJpmSApo0vi8oSsUoA7E8+6wwyaVKVMIqyXcF7XMDo2w0yR/qJ7DC8yYiaskmgFP2Ll/YDeCpkqkIAA8Rv8AgGwax4uNIZ5eg1Sb6pJEBrKASbkn45uSIv0thRS0y201dunls/3gmVcx9dGfr57tFzUFmmHI0gqGBqEUWBYCHqhQ9LSAdXxAkiMNy15eZtSvlqOVdbRmzkFVuvC2v3PvFebzVWqyinrlTNSs66KruQFJBVgrUwoAUSNz3xFLSXKtbB3G9aOC/AxJcrIGH39K2blB9GjEiVK20iIiwtAmLzsxn8heUo5Rmvr3T2hTES0lRKQ0bbKdvkf32+ce+DBcLKQ0QFFidKoxbsBf+/XBUpzB4WmT0yyAYMo8JqtuoX1M/kJ/PDIwpJCVKAe1bttCSviaQCuWklr0oHs8VZvhRCFlKtpMHVKiIkmwY9R+fuvPwplklnSNaezw7g/iiZxCSWUbD9wKtAKyoVVnhiWDAqNgg0a1adRKsoYlYk7iBrRKlgqVZr9OEMJnT5xAQpi9qPfc+7N5RPL0SsfVgCSdJYvuT9phqIHcjpvjgw5WngbENbpHJ+PRKLv4k3BBZ+vtF38FN7iegBIHob/zw6MKhvqMZB+LLeqR31gOjkNK87FXU6NQnncRqDK2mpT0A6NjqIN7RhOXJEwHIARsba1fiWp1jcxGK+WoZyQd9RQUvs5eosIZIlI6GWmUVF5iW1amm7X2G1h19LtLzoOQGpsNt2p5e8ZaMq051Cxqd/8AUGvn5MXiqnTBJaLC8fyH6nzjthvLZALKPnz/AJ5aQpmJBWQ6Rbble1dNHOsD1UCgsYH6mN/QSbf2U8ThlBZUTX0L6NuBrGhhcWCgIAo25cNq7WJsI6Tg+ZpqAlWnqX7RUw0QOpN48o98O4hE1GHBSrxUAo7d6xkSflTMS6x4Kkh73Zti9gOIL6V5WoKZLoQovGqDY+wuPvWNsFlfL+Qh1O9zYd6NAMQlZnLSEsRpcjkz1ar26tFed4iGqF1WmoKqIQGxE822kzO1h63JyW+SFJEzNmLndtA8bVZ2U/Ky5Qwszm5Ibp+NKFqg7WAsB/fXFZ80zVBhSwEXw+H+QklRcmpPe0LvpNxQ0KYVSPEeR5qLyfawHmSb4aWhckCWDceLfz5PAMIlGLWZ6gfCfDt5eR8hHB4pGsYM4cledVEP6gcvuTyx644rKaGKKIF4NQS5BpPRqibohZTNrp0kWlbXnAylw1x3rEK8nig3NmqqJlEZqlaqRNoYAxpp9T+IybW2g4eLpTl1PtGVKTLWs4ghkp8idVNbgN+sT4260lXJ0zK0jNRh/wCpVNmPovwj0xWYcoyDrzi2DSqao4mZdX0jZOnU3MJ8BjRjMSJGYkSMOJEjMSJGYkSMxI5DfKkZek1dxzEco9dh77+mMDGLOLnjDosL/c9LDjHt/hchPwzBKxc0eNQoOGg63PDlCHho8SqHqGSzHtdokm/QD/8Amx2xoYg/LlZJYsPS3r+axk4P+5O+dNLl6cVXfkL82vD3K0bXsInYhfSQCATeJtY3wks69IMM21IJqWYgfZaHDRqUkEjUhIO4JJ7DucCSgkDiKNboW2t+I6qaHJ2u/wBxE6NUSIKoYMnVEwJ6kAbWG5sOuGk4dTHOXAtGdNxSARkFT7/aCalJlaHVgQbh7ExvvhiTLw7EZg/tGZPn4wkKSg5feLKXFaAOwZdVyqlwvqyggfPB56JZlMCcwDbAndoWw6MSJuZQ8Lk1qQK0v2Q8WZGvSqkrSrKzSYVrSO6k2Im1reeBYhASp0gsw8+W0Xw82YJbT6KfpbU7nQQTTdqbWJBH2T59p2kHf8jiS5hSy07Ucb8I5OkomhUs2fxMbto8NsrxNCADIbt1ny73k2vhzEGWpBmA8w3tpcux1NS1IyMMmchYklPIvpxJtQAONAGD1gt8sjEtF+pG59e5/vthdlhWVRYkNXQG5Y7DUuDZMHSpCkZkhwDmDakOwcNc7EEO6tY5Wrl9LFZPgK5rVAD8OoQVgpOtjYHURzbWGGfloWyEl0j20qOjReXPmIQVq/5hoOJ5HYO50Zg9YSVs2zOX2J6DYDoPQQPliywlWnLhBpTywwPPiTcnd4n/AB7dSZ9v1U4CZf8A1GCPK1liJZavQYtqzK020moC2pzUJvp3PMxnfSeZbG+BoUuXmKKiwDN7/vnDU2SJ5QJiakVL9dPJtOcTTPkoOQjuGIgHvaZ/LFzPOfMG9ain3gX9CMmQkt0vX7d2jBmmsB12AEk/1wb+rmEMmkLf/T5SfEuvpFNdXO7spB6AMbARIaBv0sIA74UmTFLvUHcnu0PyZcuX9IYxdkXamirqi3NFrnt2HYACPTBpcyah8pP6/MK4mXJmKDpHfesG06bNeCfM/ucT5E1dW84GcVhpQYEch+BEGzFNTBqKWH2UBqN7hRbHfkITVavKJ/UTl/8AKlnmaRp+IaCITSehrOFn0RdTH0I/PERNlILyw7d8vWIrCT5ycs1bA6JH3MK89lBUc1qxcz1MUaYA2E1CXiey9TgRnKUSdfP2h6XKTKQEIFBFIzGXpmFC6u1NDUeT1D1OXbsv744y1funoIuwiyoa1XagSO9diRb8FlHsuIkpTr5fmKKSDw9ILqEUKYeqLAwqBnZGaNoJA0ixIIPQdZwzICWzmM6eFzF/KRTc8Pzy5ws+jHFmp5+jXZjJqwx8qkox+Tk+2L5ipTmDzpQ/p1S00pTg0M/p1kvCz1YDZm1iPxgMR7EnEmCrwHAzAuSOHftCHFIcjMSJGHEiRkYkSMxIkZGJEgzheU8R7/CLnz7D3xn/ABDFfIlU+o2/MbfwH4Z/WYh1jwJqeOw/PDnAfG82cxWFNDyqYHYnq3oI+Q88BwMgYaSZi7m/2HesaPxTFKx+KEqV9IoNuJ70EGUVSnGtRoUEao5hcTfaZ6WN2gxbAlfMmPlPiNW08uWtraxFGWghJHgSGfXm+5Nxe4FIaV+U8wRZgQ8MDHTTsetu04WlEKDgk8tOsXnZkUIYbHXpAnihEgsxWSZchVBJk73Em+0Ww4g+JwK8K904whNcpYmnHveI1G1qUCmCL6RfzId4UjzAnBhMW7v3yDn1hNUqWNO++EROVFi2gSbFy1QnYASxGk2A2PTti4BNK9Ke14GZmWu3WJZilUKg06jFwwI1MBYA8tuQyb3FgLm8YsJYQplCndd4H88TE0NYvznGabQja0MgqtZfE/hwjBl8KoSH0udWqANxeBewQpJzI9KPdg1be+kUypKChfLzZzzMOaHFUI+uUKD8NRW1UjtcOANN5EN5QThyTPE1ZE400DMRGDivhy8OlKsK7h8xe+1IMq5BhGkggiQCbx5HqMWXh5ZTnkkkO3fCF0YuYFZJ7Cj15OOp2vA6Zp0tcH7p29v7jA5WIUkODmTF5uHQo1GVY94KpZmm2oMp+s06lYyDE3Um27TFpPY3wbDFCXAavRz/AAwECxJmnKVZgA7NVhTqauS8LOL8GRQGpEmTdIllsfeLeYMi98cxKhLRmSkkvb7vtDvw9fzl5Jq0gM4V9iKVieX4WukfVI9rszuCT1sHAHYW2i53OBNxas5fN0T+o9RIwsv5Y+k9R+YTZfJwOVVUfKflfGunDTF194yJnxCVLJFzwgpMoOrH2thlGBTqYRmfFZh+kAev4glXWmpZiqgbnYeU9ztg8uWmWc0wCn0nW3vCa1rneGWVEkeIE0vRuHOKcxxBCJ8N2H3m+rA/3OQY9AcVnYuQuhS8GkYDFJLhWX19LRTSzjt/lKB/9pDUP/5XhP54DJXOZpaerQWdh8OkvOX0J86CtYFfxGZlqKxKkL9Yxq6mYagq00IQmL+Q3wsuaVhyr7e8Py5MuV9CQOX5vB+X4dWYQFKqLw7hAO0JR3HkW/fHZkgywFTSEg0rV4GjGomEpkgrLPT8mGGT4BC3crO4pKKYPmTd/KzYIJMvNVWYc/Y286cQxgC8ZPKHy5To9T6troASNi4irN8P8Lno00mDzspcmIhS2rWJvJm0C2OYkmV9NE04EfkcqcYrginEUnEqNWr4T0FAQN68IiMwKi+KCWLAwXIBIANpgQLGJG3zwh9IZrbRqFLLZ6GJ8PVqhNtIgG+8G4MRO17/AM5AOiWFjwkPYDc7QriJ/wAhQCgWuSzsKfcgQM+TQh6TqCrMHJUwQQCAytcbSCGBt0FsXUsyjkd4rJea04gimu3f6jm+I8EZSdE1F9IYDzWT8wTgqDmFIv8APSlTKp7d84Lb6SNVP/zA1Tux2NokjobbjBvmvQwoMAJdZVO9/wAxjZNXGqk3+0n+TbexxVgbRZM9SC0wdf1AdRCphgQeoOKENDSVBQcGI4kWjMSJGYkSNopJAAknbFVKCUlSrCLy5apiwhAcmg5ww4tmBl6Ipqed9z182/Qf0xg4dJxmIM5f0i32H3P7j3GMKfhWBThZZ8arn3P2HDlC/hWWKKGi7CbRIWxsCIM7nrERvhzEzAtWXQe/TbTi+0ZWFlmRLz/5K8wnrd7nVm3hoKs3Yf7lBHzBuNzYyB5YUytRPkfsbHoxgpU9VDr+r+4iqpSCbsFXoBCKfKReff8AbF0rK7Bz1J/HpFFICLlh0A/L9YlTCjmVDP3iIP8AuZoLDzE4tU0Uen6Fj5QtMYWHX9m8WUGLgkFQDqAZZZQ4WRzwAB3EYMwSWatObPt94UNb9mB01FmZlQBipUqZ1QDBmLxJiwN/IYfkSwAFE1FNudIzcXOc/LTbX7RYpwcgG8KAkFxGq7FhDAMINmE37gzIvvF/TCysOQXQe+94dl4tNpg8oG4afCrVP8wU9LFTI02iDUtzAAkEKNXY4rmBSBN+r7/iDzJZLqkVT9vZ/KH30S44lGpmBTps6a9NOqohV8R4SabNC9YAk3PacGQl73NOW9eNPKMzGyVUKWpUirkhmt1B4GOzyWRo1aAuW07lryzaTa8gAAiRcyMGVgAZnhLcu9WA4AUjCV8TVKlvMS9aDz22JJO5UHtG899GopirTkKejnl/5xb/AHCPxYzp6ck0y0qBI0sfwTwBfhG3gZ4nSEzJiSlJ1uKU0qBxIbjCenmXoPpiD91haD2PbzBjARis3hU9Onf20hyZ8LFZkpq8AQe+j6vF611NyQD2x6VGNlKSC8eMmYOehRTkNOBjmaOcQiG5WHXocY6Z89KsyS6TpqO+HQb+xm4LDlORQyqFHFj7a6nqTps5oKrObou7Db59/LGj/UDI5oSOsZH9GozcqKsen8QNmi0FncJVTSfBK6Xp+KwVWUMfrWCtPLYTOEJkxa2Sa6da38r8RGxIkS5WZQDA16BvuaB9IaZXhtIPIUMR9t+ZvWWk/LGpLloloHhD7ce/SsYK582eogrIT5U5Dt6QXxfMaKY0x4j8qL0nufICWPp54B/XLRmTpuQxpcswo9ANd6VOjAS5hBZtSxfo9XLXPKlaB/RrIhm1ydChtLHeJ56p/E5sPLT97FsNLCJZnTQ72juNmGZMGHlaXbfQdO7Q84hU8epSpUx9Y5001uAirEs8bqAe8sbW3GLM+ZNmnOeJ4Dsd2O1JSnDSwU2sBqo7eZ7qw3Fc02XraCTUXdXtzAWkjVKyRHyMDbFcP8RwqpLSksxI/dqkjresXn/BsZ85S1qBcAtsdqmgB6WpFWY4qjL3ncWn3P8Af8saUnGSAghQfQDh13+w1cnJnfDsWVjKw1fj5aOdNTowHP56o7OirTY0gQW1MIYRGkH4oI6GdrWwkTLdSkU2uW7Ma0qXMSgJmlzqbd0i7h9BpPjPylgQiGEWBERAtAFhG3acUdiCj1uYvMAKSDDmjkRpZi4AW8bGLdTufKOnmJJOMuUofMfi1WO33hDDqn4hJTIZ9M1HAuRuAaRQBRbYgnsd/IiYG8fPFzipWUCSm9ydOHNqxz+gxIWo4hVrAWNL8tG190nEsklRri5JAcWPL8bHoVU8sm5NpEg4KmcD9UQSFyvoPT7Db24PCWpkqtIa0kqQDIHQ3GpTcW9vPBGeIJqJnhWGPdj2eEF5fi6sNNZZ8+3odx/LFXUOMDVhSk5pZaJ1MjN6bap6Hf2OxxAoKtEE8opMDcdP1AbKQYNj2OLQwCCHEaxI7DXhNEIrVnsqgx+p/QYxPic9UxQw0u5v9h9zHsP+HcEiTLVj59AHy8tT1sOu8JaM5msXf4RuOw6KP1/3HDSmwsgIRf76nvgIVllXxDFKnTfpFTy0T114OYfhO8HrsO8z8/lbGaGsIemrKlOe+9NtIg9MzIN4Iv8AEJI2PqCYMyeuLggBiPx5elNNICVKJcHhxY8edecDBG1H4tRiSqKrH/UzWb/bgrpy6NxJI6AW6wA5nJq/IA9Sb9IyuoVQ76QJsxDVTPkx+A+xGLyyVKypf0T6C/nC05mc/c/xA1anWqFXSrqSw1Ly6YvzKIBMX7nsMPyAl8hDG+/Y9NozcRMyDOeXffGDXbDlBQRkVuYjOJEjU4kSNVFDAqbg9McZ4slRTUGN8P8AqIakSrBtQabyNr+UDAyguS9CGaDKnCYAFioLv+u+UdB9FuNLTco+hJi7zpO9tQupvv164hmJkJJSkvSxPLjToRw1hOfgpmJUl1AhiKgc+FX4g8dI9P4Z9MaCUwtSV2CwNWqTpATSOe5i0nvfGVPwCmVMSsKetWB75eQhvB/EQMuHVKKWDAByGHG9hrtQmOc+mSZJxSfLFCW1MTSI0ETF46yDbpBtfAJEqYsEzTV28uw0PrxYkKCZSaM50FbdbvraOTfhysZhb998aUv4dMKQyoz5n/ECEqIyPFOc+jVQMtGlFWr4fiVFUf5dp0liYNjPy84omexKl0HejRsLkOnKlj3vtC7IcQSp4aEhkpv4jI4PgMY0qG/ESSZaFgXmTi6yUG7kuz3rtwHnFUScwLBhR24Pc8YIqtqGos1NKaKadNzK1ahLK1SkFGkJFluRAmcXk0UDf3A4+5hXFh5ZQDdz66e3SCsrWZQNt5aTG3T0G5/pgszEhYIcijAjTj1sOHOFJeCUjKwDvUF6tp/43U1j/wBohfmMz4zyfhZYA200p/JqpH/EeWKyQZszxaX57dPeL4gjDSvDfT8wyTiulSokAxYbHTMKR7i427HGvOIWkAaRiSEFCn/l99t3f0jo/onXUUq2YqEBnlABfRTUXRWFyXJvIHWB1x5b4rKmy0fKReY7nSmmwp6CPV/DJsqbN+Yr/wC2Aw4m6uP5Mcr9JK7PUdt2YCAdJ0DaFleoAtIE3wvgsNllhrA8anz31a1I1Z+J8RSbkcKemvO9YSrklPxkkdix0j2H674dKlpDgN0DwukIWWJf2hlTqqs/ET16dIk7kiB+XthdK1Cgi8yQFVJix+IBLnQvr9oeRbrgqJi1WfppCUzCIH1V528rRhzpiQHIH2m5B/v1QY8wDiwvW/n7PHPlsGAp5RRTzMkFYMbCkpePIVDpQehFsdVLTqPOnpeLJWoBgfvDP+HSoV0hQsAVFBuoXmWnpkwCWMxYqp6EY5LdNzy9r62fmYXnK79/wOXCJVk8R/ITBuCL3b1J5RtbUQSMHRMIhRcgBLN33/EL8/wBHkjlJ6qB+a7H2g95wwJjwskrl2Ljuxjn8xkq1C+6feF1PqNwfUA9sddK6Q0ClUFZTiSVCFqgCSBJ6ejdPQ2xUlaBSsBOFLvLLe0EN/C07tUDHtM/kuMj5+PnfSnL0b1Me+T8P+CYUPNXnPN/RP3gLj/GErLTpUUZVAAb8TAwIHaIN9z0tguBwKpClTZxcn0Grnf7Qh8S+JDEgYfDjwPQMz7Bthp02i7LUvDSFGphBtFz1N94G3p54qtXzV5jQew089f1B2GGlfKTUi/E6+Vh+4Ly2cV5gww3U2I9R8r/AJ4EuSpF7b/uBInJXa+36i84pFjxjbwLkgD73b18sQAuw/mBqUGrFS5pTtBBsSGBUkxYRa/UTqMWUzgwlKF/avfpuRCcxYJp3358Ij4SBmZUENZlXlAjsBZT1IIgWkTfDUictAyk+dX66whiZCZpf2/EYKGqdEt3UiHHt1/2z5gYfROSb0jImS1INbd97cYHweBxmJEjMSJGYkSCPB5IO7Xk/ZE/zP8AIeeEJ08mbkTZN+J26e7bRr4XCgSDNXdVBwGp62HB4Y5R/DRhTqPEEaZ+8IJ7bGJ3wiszSoLUAOP25+Y1hsS5BBlpL+/N9vI3eLcpRUAAcsbx7fvi2HCZ00A0MKfEFzMPJKgx5wcE/H+WPTpQwZ48Pm4RztHilQK2XJPh1SDWK/5hSRKh9+bTABtBe18YxAv33+o98FPDfNZ3L5latV1IpJSFDK5ekQtV2MAMSBcFmIWZ5Q0DuqZGX6d3JPfU8WHJkTj6NTvoPOFXEODvlzTpVGUv4allW5SRsbRMXgE2I2nDCZwIJEKrkEqAPptrAdTNEgqZK2L9zJ5Un8R/Ke+KzEgEZb6bcT094vJcglVvVtA+vdomjG8/ETLEbE+XkBAHkMPSEhCWEYmMUZi3MGZWixhtNu5IAHSSTYC+5tfF1TEKOQm3r35wFEpaQFAX86NXukMOHZqhTJd2KgKWtuxGy9vfFJqFKlKzV2HPX18hHZSQqehKSzGp5VYeXIkxPiPDwqUq9WB4t4U+sT2kD269JVRMkqKpCfCpIFg4/kbQ2lGJQUzy60KJvQnjyOh22hVmRp5QQQDa+5iYkdhJPYSeYYSWj5hzB69239+Bjbk4j5acqgA3d9vbjHNVuIvrlSQFNhtMd+sH7uw26YcThkZWUKnvs31gasQrM6TQd9jpBPBcuzaqhIK6hyTpDvusn4YBbqeotGBYpaUslqte7DXi7fzF5KVKcvraznTgzwfWABLMUIX4qjDWdZN1QfZ0yBEGJFtzgKCT4QCHsLU3O7/mukRaWqW53r+oOakImozRF9Zsp7OohDvvH6Y4lR/x9PsbxQjeL8jnkIanSItE6BZZ30kWlrAAGZvG4xZSVCqvWBFIJpDSjT0iLA9Y2Fth5AW2HeLnECnhaYmtIys8DeBG/QAbk4uFPSBfL1hZmVPiQJEAMdP3ZhKYmLu06vQqSRBxZJzivZ/X7ghSEV770gPjHBaQXWSKbASxUclu69N/s/8AE4IiYoFhUevn+fOKpVm7770hBn+F1aQl15CYDi6E9tQtP4TB8sMJWlVBfbXv0iwLhxBnC+GkU/HYQCSE7kAgMR530r5z1XGfjJ/jEkdft01PDnG18MlMlU86UHW55tQcTF9ane/wzfT8oHkNh3N7RgKDSl9H719oOseLxW1bvTTjAYMuiuGZSVCuQQ6sYsG6wT+uDsyFKSwIdxcEbto/6hZRGYBTkUrYg7Pq37gjJcQ0E06jcyuRO0gdjtMg3MWIvO9JuHzALQKEd9h+Udl4lvCo1Bg7MZXxFYGXJ1m9mDMBpgbAArMQDBa9zK6FmWoEUtyYO/NwW5gbRdeWYCFVuept6+kEAtTyMfwxlZVXU6gTALMy/Go3MMsGI2wwRnmvmoa8m252d+UIhgLVFNak19AHbzhAvGG0gFeZVhCDAWTPwxDehOkdAMMf0ozODc149dOd9zE+d4WI5cPzBvDOJB3VWVg5MBqe9+wIaCe8GT2AxJkkpHhPn2PtASpP+UMalVSdFQqakhVGtPFJiADpJBJMfHHtgiFFCSoGm1Tr+PaM1cgqWAgNxNE22LNW5FawM+XPS9pj7QjeRJ2m5BI88OAwkJodlU9vP7FjwinHYLFlBJN9hvG58vfb/rC+JnfKQ+unPusNYPDGfNCNNeXdIOoU9RIJk7+X+kYxpc3IX/nmY9LNkBYCQwby5QYtNwQqiBUBBFpt3/ni2eUtBVML5NdKwsuXNlzUiWls1xrTf3i/LLsT74vhFZJoMI/F0FeHUBt7Q7p5dIFgffG4pE1RJzqTwCXHnxvHkkTJSUgZEq4lbc6cLesefV8swDAcys0sQPrAOoAmDYQNiOxwJclSax6CRi5a2BoYlQB1iosrptTiVP8Aq7jsPIE9cDCCRBjiUoo9dYJ4nl666atRXJqfAT/6htYH3E9hihKUuD1g0smYQrSAKNPzkKTf7zbM3oPhHvikpJUc519BoPuYLiJqUj5aTb37oIJpi4kx54YUopSSA8ZoSlSgFFoYUcw1FWamYkqb3Fpgx8LHc8wtAOKS15yEK6t60uOBF4k2XkeYOj83FbG1QWZ7QSatM5Z1DK+s6US4KEgS7KRClYsVLai9zClcCnrUhQTUAVffhzJ0/UMYGQmYkrIGY3G3HkBY/d4WpU5AoMqGIQT16kDpMdPWDGOTC+jKuSBf9weWShRIOZFgCahvttCXOV+itI2sbRP7/l6xi8mXlqbx2dNzsGgJlnB4FDHLZ7SoVTpsFF+UFjLVG7kdB097KTZDqzEPrx4AQ1Kmj6Xb25nlBtKgAwHw0qIlSbamidXooJM9ySJFsAzZgSPqVfgNvtyDXgqkqSQCKC3Hj9/1E8hlqWZPiuhOk6QoaSqpzvUZNMFQrAaVb4j2IwZlShlzcXbo3MmxhZawpVBw5k/YAF+kT4NWMs1jTBPhqi6QeYrrI3lr6VM3VuoGBzQAw11cv0f3PLeL3drd17+0OkzU/DBFgsfakTM/dgzPXAWa8VKXinOlnQgETpKggRqa8ewOCIISXO7/AKgZFR31MUDOAw0daToZNhWHh8wMjl5jAjcYuElJvu/T89YqoApbvtonnE1sVJkOrLOx5hDNHW/gqPU4ifCmmnY9HjjuXPf8kxrhmYbwkdSQxADrE6tLDXrU2aSrAAzcjEmgLJSe/wCHjiP7SswLd08zFVSpqQrX5RTJllLMrIFW3MCYLM/YAiCRN004YJZUu53ah6N3WsbSviE1ZKZpcP5+Y7ELanKFiAsWaeRp7OCdMEkCQB2GDBBJOap9R0YO9z7xDiJbAJpTXXq5ZrDhpG2oq3Iw0E7AjY25kAIBYCIg2EziwzJ8Qq3rwNLHlygClgnKbH04jjFmQzKKCtdwrMGGtqa1KdSkL6Domorsy6ZUiATecGYEPLFrhyK0Iuw5wosHN4jyO1wSelgz1gOoX1NUoBTSLEikpJ8MMZ0gHnA9NwLiLYjJICZtFb78dvO2hesWzG6LbQ8T6UUDSAQeE0eGFIOmnTsW0uouXb4rLIEMTAwOdhlqPA1PT6RU6X1rFcOoS6k2FOZ+pWzmwGgs0Kczwmm41UzoJE9NJ87Wjuy8osACcWROmIoqo9e+ddSYuoJVakU8GoNSzNMVAVDk09XbxFKAg9CNQPQjywdawuWct7+XfKAKTlIJhlwjNVajnxlBak5E930hCsG1woB6XWwZwcAVKlpAyWIHkKjv7Boutay7mtfW/pDCoqmGkm45lMGYBAHUfEtokzHci4mm3K/P9HlCJwoPkRzo1eFesDZmjceILFQxfYgRuYJDi06jBMnaLuYacmZQnUwjiJKpJ/t7CmjnbZ3De22LlCogXG5PXy6xF4m4BkTfGVilqmrzCwt+W+3KPR/DzLkS8qiyzfhsAe7xPLtpZWIgbeSjqP8AVcYSWHBSL9+kaqSzLanfrDXL6HPUEfl6f0xVSJ0munvzf7061gS50ianLrttyavkX6Ui1qUFheDcT54aRvrwjJmKcNpx79dbiL6TyBfHqZM95YMfP8RK+XNUjYwgRRBJv0ib+uOKckAU1/UaqWCSTy/cUDNpTdSSpYEHSbz5aRcg+WOLUkaxeXKmLsl/aJ8f4vUzdUOwKQmikm3hoPjqQbhmJIE3v2xlpkhay1nc/YRvKn/Ikh7gMBxhLT4ghYIoMbCNgB5bxHXDQUmwhReHmBOdRrDDwh1xCCSQmAhYABXBKZIFZBaNwPyuJgmbb9PbComzApiACL8dem9X9yHTJlqSCCSk1HDTqXpRvYGvw3UkoqtAO86djvcH264Y+YkpyqoT3xHXSFhKUlecVSK0Onoa7XOkLs/mbvpTw1hNN9UwZaTAFyQIgWvGACUoL8Vb9NhGgmahcsZTUMOe5hPg0cjMSJGYkSCHbTScH7QA85EkD0BOr2PcSo5XNBGn6c/by4xpfLEqSyrn0Og6X8+EWNT1eFQJKhVlwoJub/8AL1sJ3xwTCM0wB3NNKfj1gZk1CbUrDhWAAUdN4MxaIHUqAsdyFY2dRNBWvffdjASCO++67wRkq6kwDJJOo2tpJJnoYJExaX1KRqIxRcs98f48gxtHQule+3i7M1iFEWLsBPUSY1et7HeSJkTgYTWv8t3+ItmDQqzkkBEEGqWpj/6dOiYPmTuevbcDDKKHMrSvMmKKbSGWbqaisQSSCO0XK+2oB5G6026iMUTx73/HWBsztGuD5lQ7lXEGoWA688+UaZDOImxBwRN/ENGPHt2PKAYuWTL8JY3HAixPkDDVqIqNMwTsR1I2w1PlSsiTLFNdgG1jIwmLxCFqExTnYu5JIDA6XetGEK85whqZJUFCTfSJVvVdj2kQdyThIKCkuCFD1H3HIxuIngnKoFKvfkbHpCsD4UIVQ9lHxUH9OqXNunW+CDcadCPzBCWgfiBanoqAKUaVK1Arw6yCpJGogdCfy2wRKQp0k14OKQNMyrjvt4U0qpUgqSCOoN8HKQbxwFoO/jEqf5y83/uJZv8AcNj6/LAPlqR9B6GCZwfqiaJWpKzUX1U2EMyfqpurDuLjuMUJlzFATAxFn/OvL0i4zJBKTQwTw/jIZ4rmEKqkqI03HOR1MajbrBib4rMklAeXUuTXrQbVZuEczBfhVQMB7VPR3jpqlJW5gB9ZpO1jrAdywP3gxEbkaewID9JbbseUBSoqSCe2oT1aFudo1gg+JT9V4iKkV2BVXOm1zNVmJNjqHQX74Qo0rVibA2D82HluYLLVnAq4pQagOSRyc+8NAo6DUCZH4yP5KLY69IUZ1V74xXRogKFXYLpXty2L+g2/F1nHSp6mOEVeJU6StUEibErI2gQCf/KB2JG1gWUhJdw/DeFsXiJ0tKcqsocOduw7wyqZZAD4ZbmIUqQDbTdie5b7IFh1OGkYMOmZNSzVv9PYhGb8SWpKpctRL+G31cRtwF4hpIIDE2ECf79cAxmHSCFyxRVaa8YPgcacqkTSXTvpo3SFub4VSqOXZZJifYR+mBoKkhniysbWghUtE5lj8bU0OiKRGrVYlnXc0wCbiNjfbDM6aEh0lga1to/6hvDSCGCg6m/LAeReB8lSnXzgIGIUUhoDAEjVMaoPqMXw8pMxOZV4rjsQuSrIjzgitlRoZUEFhuSST6kyT2w0ZYyEIjPRPV81K5tWizLVgKKU1pGm0EVHLAlpiywdjABnpaLnCaJCgfFGni8chYaX32O6V6Dhf0dDCnUrOFVwSEB5iOnSwO4PUYQ+JfEThApEsOph0J36faLfDfh39YQtZZL+YG3V3hZxFRQqFKb61HfoZIIt1BF4jDGCmHGSRNmJyq4e9dK2LwPGy/6Kd8qWp08e/UNA2bzQKyTvOruAIsfImO364sP7aso0Ibjv1annuwsXmodiXBJtStNLPWnDZzzObrajbYYYUXi0mXkTFGKwaMxIkbBNoEsTCjz7+gwOYaMevKGcOmuby5/gX8olRKjn3VLJ+Jz1/X0C9sDUCfDqb8Bt3x3gwIHj0FuJ374RrJVSx0gXYy7Sbibcs6SZMAEEEkY7MlgeLawpTrfnwiqZpIy73Na9LcoY52sUQETLWXre1wdzHLB6nQfiVsClJBVl2v33ro0cmEhObvvveNcCRlZkZSNJkggzBERG5l0pC3n0nF8QQGO9O+jwBHiducOcy2pGAPMRIPdlMqF8gwE4AzEE9jWOpiFSjI8SQiawwZrQtZNJAtZtTFr22xQTGOUVLacDflpBfluCTQcfbyiRqRpYwNLXkbW1x/tolx6nFhUsO9PUsYpl377tC/hrPTzDJpJuQHMkhVgqoJMRGkbWLYZSRRQPSlzc87wvipeeUoEdeluVo6qvRCJrJ+I/De472NiPQT645ipkqRiAggkqD/8AaDQeoMJYDDYrHYYrQpKRL8If/IgOangR7UiunxI6DDho6Gzes9sRchAXmSHDXfU0ty5REqmMETaKJsBoPFfiefSOVqn6uoBIKVEqra6hxqAj8IaoSO4xZNweDeX5pD5gnitNKgADDSGFSQsMEeZNxcky3XoMSQlVSab1fb+NHNdYXWsIUAK6bVBp6c2HKF5YfdEREG8AbCd/cXwVRzF4IhOUNA1XKA/Bb8JP8j+/zxXMRfvpBQAdYu+j3+aT4hQopaI+PSRyEkhVBn4mMCO8Y7MQFpynpzii1mX4mPFv1WD8nwpWzlZWKNSpVGJ0sCrcx0qCOh6kbKG7YVXiQiUk6m33PfCGDIWolhQX4fvTnyjpa2Z0sCwVr6mDyFIF+YjYH1IChmWykYAilR33+jeBzJWdOW3LukEcR43RZCjOUJmfEU1DQSGV6iOrK3xM1PQSTqqMBZVwRKHajj31brfzNzFAgh+VK01HkB/8R/jCvNZ9UJ5Ai6lUIkmBOgIgJLXKkwbgpVHRZiUqUX5/nvpxiykJCQB/MEgz2MxYbG0qg8ouT545A2Mb1QQZkhpnudif9KqT74JLXlUDC2IkiZKKI6DKq6r4jURUogiZ+zLRIIMqSREnv0kYcmTEElSaFVK2UWYb27eMWUiblCZlQhiWulLknapYm5I4QBmKw5rb/DJki8i/UxacFxUomUhRV9Omh/iKYaalS5iEp+uxJLi59db84E8Qd8LjlAykwvzKq6DLjR4dPwkar8FSkgZyF8MQGqVANRYFrb3jFJP91QUdfVgadOOuseonKMhBIvpwch1H2A20i3L8KNSqUoISDJSYB0jYm8Cw2w0nES5csFVC7MK12/MZkyRMmzCAXAALmlND1egvwgbO0WV/CcaXSVbUdo/IYsiYj5ZmJLg1oPtd3vFVylGYJaqEBqnb9Wakb4OtM1JrMAijUZ+1FgvuTHufLBCWGaKCWVkITc9v9+TcY6jK5h8zVFMMit8Tvs1OkJlgB2jSDuN+mMLE4WSucZq3a6tuXXyj08uYuRh0yJIBUWSjcnfkLmFn0zWmSGRQhUBQkAQosoPSepJ6yNowLB/EJilqU3hL9GguK+ESghKHqkCuqnv61jhM5UUnbm7mD8uov6X+Z1ZZJrCMxGXwwJgkUjMSJGDHCWiyEFasogjJ0PFbQj6RHOYnSo3boSt7gdJN9sLTDkGdQc6fYfgmNBJztLllhY/l/cCAs3VBIVfhUQPPuffB5aSKm5heYoEsLCLsrVVEJsSSwKyQYKQDPkWa3eMVWlSlsKWr1qOoiJKQlzXh0ofOK1zbeJ4hgtOq4EE+Y2wRKAlOUWgMwlb5tYf/AOINWiq6qsAhQOp2LX6dADI3nocCyWQO9v357wEkSwTv335CwEDUuKgNLIGgkqws4lStjeRfYjoL44uU/wBJ/HlvBZbhLK768PWL8tmfEphGjU4emSbsLEpcm6qAR64AtGRWYWDHhx6mGEqzDt/4pSCaNcMhYzDLrPUWIaoPfWacdlwNSWUw3bzoPIB+sdG/fbxWS61keSV06WvbWrQYE/aZFW2CIUlmsXccv0CYHMllSTqLd9YezylgVKtaNzjRzSp8wBSXKQ4On8x5sJxGElHKtsxYgXpUHl1gemgEx1BB9Dv+WJOwktYrpUc4JJ+JT0KvzppCmvUIcIx5GFRW9TDkzv1dB/pwilIvrTv7xuLVTvusAK7BFRhzKIPexMD2w0qlBC6QCrO9NPz19ohisFjMSJGHYj7wg+mKlIJBOkWSspcDWGHD8+tJAoWy3MXLN39YAAiIvG5wnPw65hcl/sNu7w5KnyxYNTe578oYZbM6iWJKjWwkdNBaT2MAUiLfEW6OwK75GTwHq3/9dANhBFylfU1HPp2IHyuWcvLKdUhiFvdZWnTWRBFMCb7uUB74ZM1AS70+2p6+1oWyElmrGUE8SoWNlTUBBMagAHcNvCgLTVt7B91bFycqW39tPyfLUQNng5VbmcjQE0zq5QgJ0rqG4UayD0GqqLeGuAqmJoBUkEhtW202bpuY6JRPAOx4RtHhTrMqDUUn8NI6dJ6S5So9ugOLO6mAa3r+HaBKQwBe/pDfKVj4Zm82YgmCyWNtjfv2GNHDyTNUmYTQPRvvyjzWKmiR8yQkVUQXfTZuJimvsTgWKn/MmZRYQxhsKZUgrNz6D9wMlB2EqpI7gYaRhipIIhBc5CSxMdJ9JvoYtEV82hC0z4fh06aneYLPJgEkxIgQATJ3yJGN+VlSr/LfYh6fYR6ufhBiqooUhhxI34cY5zK5mmiOz02NVxNGsjadO4NxuJFwLHY2wbESFYhYTLLAAUL0B/6dSRQFw2hgWFxAwiSucCSomzVI/wCrQPzvaAM3mNUmZZ/iP6f9Y0USwk5WYCiR9++cZypilDM5JJdR46D7+mkAVKjWgkR+t8XCQXO8TOUkVtaH30YzdTKhiySMwF0liIITYR8QWWBmY8rzjL+JYcLlmWk1oSNx2DGt8LxjThNWHFUg/wCpuf3+bB8cruztq+L+79haI6bC+M7DpSACLd9/iN9S85Na9+UcdUY77gkx5gdY6C3XbGyg0aMmdKrmBu7cW4XHWMVpxeFiGjeOxyL6XLe89Inp6A9xheZ4zl017eNCQn5SM/8AkbcB5axfVyyPvysftKN/9S7Hv0MbnFAtSbeX7jpQlV/OIU+H0luxZuu4RSPzn5jHfmrNqev49jAzLSO2i+rwMtTFRV8OZsTqUhYlvvovm40+eCCYRQ178oASDbl9+7wr/hGFRUcFSSB8+oOx9dsFzBiRFIOzVewC2EER0joR7D88VSCLwMJBU+3f88YCx2DRtTFxiEPEtB3Dc2wdREi8/mZPoWPz9MK4iWkIKna32p1YdvDeFzTJgQz36XL9O9ItbPEOiwSR8DBQWk8hGkghgxXV56scTKzpPqPUeTt0iswiVctS+wqDDXL1HDMpGioBJEEA3vqQ3UiRI8xtgkpHzPpPfOEMXMEkDOHBg6hngouuhibtusdf0xxRXmPzKsKC1d35U4QJEmWUJVIo58RuWoWY7EO2tjSFHF3QVJVtiDI3BAOkEDvqqE+2Ood3If27doOlJ+WBbTi38e8LiOsyO42/78jfBApzxjpS0RxaORvEiRmJEjMSJBHD6RZ+wW5PkGU+lyqj+mFMWpKEObmg5sR6Akxo/DZcydOCE2FTwAIPqQBHRcJo1SOU7ElEMoajANLoxGkgO977qx2XGXMUkEblq3YOKNyHkRqY0FYd3AqB0q1+XpQwK1RRUANNkNEgMmkrKsjb21eIAzPEfE5G5EsAqyNmop6mpcEPwy6cg9hCKpSQXaoa1Balqvqf3FlTLK9TxgOYoVM8wkuxJjrIYQNmGoDcHB0LISUvR6aMGFO7GFFJZqc+J3i003KhdWkGHVZktf4gYvEapO5CG2tpiGUslKXNQTy09ffaAzliWllqazPx19IYpTAhBsAP7/vtjRXN+VhhRirTUR56Rh/n4xRUcwBvoWt5xmbACkkgAAkk/wAzjMl1UBGzOSopJAelo3mfofXqtrouXpkAKyVoVtICkqAYgkE43FKcuFMIw5c/5Sci5VQ70B13j0LiHFHcZk1KIOWpg02AIkkIS0qfsxbHhcQibMUJqVa+VaddfKPf4eUhCQk3bvvnHjmZplnbmOtQT6qiySehIVfUxj08hSmCgL1JfWMzEpTWWqooEhogjuoDTE2BGx9sOfMlzFGWsVb3jIMmZKSJss+F99oqIMQYm+07STN79b36YJKdAY1gE4pmKzIpDH6O8WdMx4tQeKgTTJ+Kmu0qDY79e59MKY+UZktSEfUr7X9I0fh82WhSVTfpQfUuz71f3uBAuZzEsxOxuYJNtgsm5FuvTCSUqCQFX76PGupCCSZZ/n8QLVywYg7G58gDH52HyxdJa0UK1WVp9/4hZnMlClh2Mecdf6YYRMOZjFJiElLjvvaB8upJA7gfynBVrygwCVKSpYCrRe2xYwB33I+UH5E4EkNQV770hqYsqOZVPt9/WLsvUDCxnp+v9fkMVUkpvHEqChSD6vDKnhLUR1/y3rMkQNCmJVpJ1GGtCxHmMd8KSyht626dtC/zCu3Fv/G/rBNfjCsiqEamziNA0kLTAEKjSJ1tdpCkixLDHVVfKef45AW46PWBy5eUgqs1PueZPpbWE1SsFBpMNJU3QTY2IZTdRG0ALviyDm8YqDr3WvWOzE5aG4Pn/EBs0nBYqAwiOJHYzEiQxy9MKkmxI1E9lF/0n5DCExWeY2gpzPdPWNzDyhIw2b/JYd9k38zc9AYEyWa+uFQqrBATpeSoAFpAM2JBt64ZmIaXkBvteM2WvNMzKFADfbSHmWcnQSGhFIXWVLFqhl3ZlEkbQGJi+By8wL0fhSgsPesCxSJaktVrl7vr9ocUkRTUp1VIKzbVzGJsCFKyBfp644uYUSzNJdRZNRR3vyFqQmiSZ05MpHhQHUGOmUU5mhr1he3CRVjRvpuNrQTAJ3FjY2xVE0mb8sJrXUWGvdYbmhMmR86YsEBhYu6rDukK83kKlFmB5WFjEHc7ETB7bkeQxb5iJgGo77+8EyERqoqmbaGAkr0ifInv39sdQtSWBLjf82ikyWkupNOHM6fuKXQgwdxhgEEOIWIYsY1jsSNYkchkqaFCCzWZt52sAQegPncnGRNX82ZmNhQfejan0Aj2Xw/C/wBPIA/yVVV34BwdBzDkwdkeKVKainC1KfSnUEpYzAj4YJPwxYsPtE4AuWFEmx1Iv6/z7QwqS6QE9NNOA0po1G4gGkpJ5mLMZLMxOomRqJMzMx/+s7oZOpWw5Dzb7/8AqB+qM5UjLQ92f7f+lvpq+4QU8RRUKgXAV1LIxidDBbhSASYkWsJtgaFEVHfHuvMRnYqSCGG+lDy+34htxLLpRYoFZGJDMhIaxEalcHa4GkgHVrO0S9hiRMzC7EDhzH328hgY9IVIAUfDmBLXI+1K8+TmpQskrMdJ3wGbNmTC8w1hiTh5clLSxQ1jcSRePPF5MkLBJS4GkK4vEKlLShCspOvfH0fWFeY0FiWCkzuVufyxuFEoUaMNC8Rl8Ki3OP/Z"
st.image(img1, caption="")
