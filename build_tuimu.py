import os

questions = [
    {
        "num": "01",
        "title_1": "Thế nào là",
        "title_2": "Video chuyên nghiệp ?",
        "body_left": "<p>Đưa ra ít nhất 2 lý do theo quan điểm cá nhân.</p><p>Góc nhìn của bạn, không có đúng sai.</p>",
        "body_right": ""
    },
    {
        "num": "02",
        "title_1": "Thế nào là",
        "title_2": "Video hấp dẫn ?",
        "body_left": "",
        "body_right": ""
    },
    {
        "num": "03",
        "title_1": "Khi nào bạn cần",
        "title_2": "\"Lộ diện\"",
        "body_left": "<p>Kênh của bạn hiện tại là một \"sạp hàng\" hay là một \"ngôi nhà\" có hơi ấm của người chủ?</p><p>Khi nghĩ về bạn, khách hàng nhớ đến một món hàng... hay nhớ đến cảm giác yên tâm khi được chính bạn phục vụ?</p>",
        "body_right": "<p>Tem xanh mác đỏ phô bày,<br>Không bằng ông chủ tự tay làm liền.</p><p>Khách hàng quyết định chi tiền,<br>Vì mê sản phẩm hay ghiền người trao?</p>"
    },
    {
        "num": "04",
        "title_1": "Mua Thông Số Hay",
        "title_2": "Mua Người Quen?",
        "body_left": "<p>Bạn đang nói chuyện với khán giả như một người bán hàng xa lạ, hay như một người bạn đang chia sẻ trải nghiệm thật?</p><p>Điều gì trong cách xuất hiện của bạn sẽ khiến một người lướt qua cảm thấy an tâm và hạ bớt sự đề phòng?</p>",
        "body_right": "<p>Máy ngon thông số rườm rà,<br>Người dưng bán rẻ chắc là rủi ro.</p><p>Anh em đồng nghiệp chẳng lo,<br>Chuyển tiền cái rụp khỏi đo nghĩ nhiều.</p>"
    },
    {
        "num": "05",
        "title_1": "Bán tính năng hay",
        "title_2": "Bán Kết Quả ?",
        "body_left": "<p>\"Trong 3 giây đầu tiên của video, điều gì ở sản phẩm sẽ khiến một người lạ cảm thấy: Đây chính là thứ mình đang cần?\"</p><p>Làm thế nào để người xem nhìn thấy chính họ đang thảnh thơi và hài lòng sau khi dùng sản phẩm của bạn?</p>",
        "body_right": "<p>Khoe dăm thông số nhức đầu,<br>Khách lướt cho lẹ, hơi đâu mà nhìn.</p><p>Làm clip đánh trúng niềm tin,<br>Nói câu kết quả, khách xin chốt liền.</p>"
    },
    {
        "num": "06",
        "title_1": "Tin lời nói hay",
        "title_2": "TIN BỐI CẢNH?",
        "body_left": "<p>\"Trong 3 giây đầu tiên, góc quay phía sau lưng bạn đang kể cho người xem nghe câu chuyện gì về con người bạn?\"</p><p>Làm thế nào để bối cảnh video thể hiện được sự chỉn chu và uy tín của bạn mà không cần phải đầu tư quá tốn kém?</p>",
        "body_right": "<p>Lên hình chải chuốt bảnh bao,<br>Phía sau đồ đạc lộn nhào ngổn ngang.</p><p>Khách xem bỗng chốc hoang mang,<br>Tin lời bóng bẩy hay càng lánh xa?</p><p>Khách nhìn bối cảnh ba giây,<br>Gọn gàng ngăn nắp tin ngay tức thì.</p><p>Dí tường góc hẹp làm chi,<br>Kéo ra một mét phẳng lì hoá sâu! 🚀</p>"
    },
    {
        "num": "07",
        "title_1": "Dùng từ chuyên môn",
        "title_2": "hay đời thường?",
        "body_left": "<p>\"Làm thế nào để nói về một sản phẩm phức tạp trong ngành của bạn sao cho người hoàn toàn ngoài nghề nghe xong cũng hiểu và tin cậy ngay?\"</p><p>Bạn thường dùng hình ảnh so sánh hay ví von đời thường nào để biến những khái niệm khó thành câu chuyện dễ nhớ?</p>",
        "body_right": "<p>Khoe khoang từ vựng cao siêu,<br>Khách nghe chẳng hiểu mọi điều bỏ qua.</p><p>Bình dân kể chuyện thật thà,<br>Khách ưng cái bụng, thế là chốt luôn.</p>"
    },
    {
        "num": "08",
        "title_1": "Làm video lướt qua hay",
        "title_2": "tạo tài sản số?",
        "body_left": "<p>\"Làm thế nào để mỗi video bạn làm ra trở thành một 'tài sản số' bền bỉ mang lại khách hàng và niềm tin ngay cả khi bạn đang bận việc khác?\"</p><p>Nếu được làm một video giải đáp băn khoăn lớn nhất của khách hàng mà bạn có thể gửi đi gửi lại suốt nhiều năm, video đó sẽ nói về điều gì?</p>",
        "body_right": "<p>Viết bài ba bữa trôi xa,<br>Quay phim để đó, tháng qua vẫn lời.</p><p>Xây kênh tạo dựng cơ ngơi,<br>Ngại quay sợ xấu, đánh rơi khách hàng.</p>"
    },
    {
        "num": "09",
        "title_1": "Để máy im hay",
        "title_2": "chuyển góc liên tục?",
        "body_left": "<p>\"Tại sao quy tắc '3 giây đổi cảnh một lần' lại là chìa khóa sống còn giúp giữ chân người xem xem hết trọn vẹn một video bán hàng hay chia sẻ kiến thức?\"</p><p>Nếu bóc tách 1 phút video về sản phẩm của bạn thành các chặng 3 giây, bạn sẽ phân bổ góc nhìn (người nói, cận cảnh chi tiết, trải nghiệm khách hàng) ra sao để họ bị cuốn từ đầu đến cuối?</p>",
        "body_right": "<p>Đặt cam đứng sững một hồi,<br>Khách xem buồn ngủ, lướt rồi bỏ đi.</p><p>Ba giây chuyển cảnh tức thì,<br>Mắt nhìn cuốn hút lạ kỳ làm sao.</p>"
    },
    {
        "num": "10",
        "title_1": "Xây kênh lẩu thập cẩm",
        "title_2": "hay đào sâu một ngách?",
        "body_left": "<p>\"Nếu người xem chỉ nhớ được đúng một thế mạnh vượt trội của bạn so với các cửa hàng khác trên thị trường, bạn muốn họ gọi bạn là ai?\"</p><p>Khi lướt thấy video của bạn, bạn muốn khách hàng nhớ ngay bạn là người chuyên sâu về giải pháp gì?</p>",
        "body_right": "<p>Ôm đồm làm đủ mọi ngành,<br>Kênh như tạp hóa, khách đành lướt qua.</p><p>Đào sâu đúng ngách chuyên gia,<br>Khách vào trúng tệp, thế là chốt luôn.</p>"
    },
    {
        "num": "11",
        "title_1": "Đợi đồ xịn hay",
        "title_2": "dùng luôn điện thoại?",
        "body_left": "<p>\"Điều gì thực sự đang khiến bạn ngần ngại chưa dám rút ngay chiếc điện thoại trong túi ra bấm quay mỗi ngày: là do camera chưa đủ xịn, hay do nỗi sợ hình ảnh mộc mạc chưa hoàn hảo của mình khi lên sóng?\"</p><p>Khi chính bạn lướt xem video mua hàng của người khác, bạn bị thuyết phục bởi sự chân thật đời thường hay bởi những khung hình dàn dựng bóng bẩy trong studio?</p>",
        "body_right": "<p>Cứ chờ máy xịn đèn to,<br>Đợi mua cho đủ, buồn so tháng ngày.</p><p>Người ta điện thoại cầm tay,<br>Bấm quay mộc mạc, khách bay về liền.</p>"
    },
    {
        "num": "12",
        "title_1": "Đọc máy nhắc chữ",
        "title_2": "hay nói tự nhiên?",
        "body_left": "<p>\"Điều gì thực sự đang khiến bạn vẫn phải phụ thuộc vào app nhắc chữ: là do sợ quên từ ngữ trau chuốt, hay do chưa tự tin diễn đạt bằng chính ngôn ngữ ăn nói hàng ngày của mình?\"</p><p>Khi tư vấn trực tiếp ngoài đời cho khách mua hàng, bạn có cần kịch bản không? Làm thế nào để mang đúng sự tự nhiên và hào hứng lúc nói chuyện đời thật vào trong ống kính máy quay?</p>",
        "body_right": "<p>Mắt đơ đọc chữ trên hình,<br>Khách xem thấy gượng, bực mình lướt qua.</p><p>Chỉ cần gạch ý nói ra,<br>Tự nhiên kể chuyện, thế là chốt luôn.</p>"
    },
    {
        "num": "13",
        "title_1": "Nặng về quy trình hay",
        "title_2": "bấm máy quay luôn?",
        "body_left": "<p>Theo bạn, một người làm nghề cần chuẩn bị tối thiểu những gì trong đầu để có thể tự tin rút điện thoại ra bấm quay ngay một video mà vẫn nói gãy gọn, đúng trọng tâm?</p><p>Trong ngành của bạn, 'món chính' mà khách hàng muốn nhận được ngay khi bấm vào video là gì, và bạn có thể lược bỏ những bước thừa thãi nào để đưa nó đến tay họ nhanh nhất?</p>",
        "body_right": "<p>Vừa lên đã vội xin chào,<br>Khách xem tụt hứng, lướt ào cho qua.</p><p>Ba giây nói thẳng tuột ra,<br>Đúng ngay nỗi khổ, thế là xem luôn.</p>"
    },
    {
        "num": "14",
        "title_1": "Tay chân vung vẩy",
        "title_2": "hay ngôn ngữ cơ thể?",
        "body_left": "<p>\"Khi muốn khách hàng dồn toàn bộ sự chú ý vào điều quan trọng nhất, bạn sẽ dùng hành động cơ thể nào thay vì chỉ nói bằng lời?\"</p><p>Một cử chỉ dứt khoát nào của bạn từng khiến khách hàng ngoài đời phải gật gù tin tưởng và ra quyết định ngay lập tức?</p>",
        "body_right": "<p>Lên hình cứ đứng nghiêm trang,<br>Tay chân cứng ngắc khách hàng lướt qua.</p><p>Nhẹ nhàng cử chỉ đưa ra,<br>Tự nhiên lôi cuốn, người ta mới dừng.</p>"
    },
    {
        "num": "15",
        "title_1": "Tại sao cầm sản phẩm lên nói về nó",
        "title_2": "là sai ?",
        "body_left": "",
        "body_right": ""
    },
    {
        "num": "16",
        "title_1": "Làm thế nào",
        "title_2": "Video đẹp ?",
        "body_left": "<p>Khi đã biết cách dùng capcut & quay bằng đt rất nét rồi</p>",
        "body_right": ""
    }
]

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Túi Mù - Bộ Câu Hỏi Offline</title>
    <style>
        @font-face {
            font-family: 'SVN-Integral CF';
            src: url('./assets/fonts/SVN-IntegralCF-Heavy.ttf') format('truetype');
            font-weight: 900;
        }
        @font-face {
            font-family: 'FD Tiempos Text';
            src: url('./assets/fonts/FDTiemposText-RegularItalic.woff2') format('woff2');
            font-style: italic;
            font-weight: 400;
        }
        @font-face {
            font-family: 'FD Tiempos Text';
            src: url('./assets/fonts/FDTiemposText-MediumItalic.woff2') format('woff2');
            font-style: italic;
            font-weight: 500;
        }
        @font-face {
            font-family: 'FD Tiempos Text';
            src: url('./assets/fonts/FDTiemposText-SemiboldItalic.woff2') format('woff2');
            font-style: italic;
            font-weight: 600;
        }
        @font-face {
            font-family: 'FD Aeonik';
            src: url('./assets/fonts/FDAeonikRegular.ttf') format('truetype');
            font-weight: 400;
        }
        @font-face {
            font-family: 'FD Aeonik';
            src: url('./assets/fonts/FDAeonikMedium.ttf') format('truetype');
            font-weight: 500;
        }
        @font-face {
            font-family: 'FD Aeonik';
            src: url('./assets/fonts/FDAeonikBold.ttf') format('truetype');
            font-weight: 600;
        }
        
        :root {
            --bg-color: #ffffff;
            --text-color: #1a1a1a;
            --accent-color: #000000;
            --line-color: #e5e5e5;
        }
        
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'FD Aeonik', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        .page {
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            position: relative;
            padding: 40px;
            page-break-after: always;
            overflow: hidden;
            border-bottom: 20px solid #f0f0f0; /* Screen separator */
        }
        
        /* Header */
        .header {
            position: relative;
            height: 200px;
            display: flex;
            align-items: flex-end;
            border-bottom: 1px solid var(--line-color);
            margin-bottom: 60px;
        }
        
        .number {
            font-family: 'SVN-Integral CF', sans-serif;
            font-size: 280px;
            font-weight: 900;
            line-height: 0.75;
            letter-spacing: -0.05em;
            color: #3f3f3f;
            clip-path: polygon(0 0, 100% 0, 100% 82%, 0 100%);
            margin-left: -10px;
            transform: translateY(18px); /* Shift down to sit exactly on the line */
        }
        
        /* Main Content */
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 40px;
            padding-top: 10px;
        }
        
        .title {
            font-size: 64px;
            line-height: 1.1;
            letter-spacing: -0.02em;
        }
        
        .title-1 {
            font-family: 'FD Tiempos Text', serif;
            font-style: italic;
            font-weight: 400;
            color: #333333;
        }
        
        .title-2 {
            font-family: 'FD Aeonik', sans-serif;
            font-weight: 600;
            color: #000000;
        }
        
        .body-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            margin-top: 20px;
        }
        
        .body-left p {
            font-family: 'FD Tiempos Text', serif;
            font-style: italic;
            font-weight: 600;
            font-size: 26px;
            line-height: 1.5;
            color: #1a1a1a;
            margin-bottom: 24px;
        }
        
        .body-right p {
            font-family: 'FD Tiempos Text', serif;
            font-style: italic;
            font-weight: 500;
            font-size: 26px;
            line-height: 1.6;
            color: #4a4a4a;
            margin-bottom: 24px;
            text-align: center;
        }
        
        /* Footer */
        .footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid var(--line-color);
            padding-top: 20px;
            font-size: 14px;
            color: #888888;
            font-family: 'FD Aeonik', sans-serif;
            font-weight: 500;
            position: absolute;
            bottom: 40px;
            left: 40px;
            right: 40px;
        }
        
        .footer-center {
            text-align: center;
        }
        
        .footer-center span {
            display: block;
            color: #b0b0b0;
            font-size: 12px;
            margin-top: 4px;
        }
        
        @media print {
            @page {
                size: A4 landscape;
                margin: 0;
            }
            .page {
                width: 100%;
                height: 100vh;
                padding: 10mm 15mm;
                border-bottom: none; /* Remove screen separator when printing */
            }
            .footer {
                bottom: 10mm;
                left: 15mm;
                right: 15mm;
            }
        }
    </style>
</head>
<body>
"""

html_content = html_template

for q in questions:
    html_content += f"""
    <div class="page">
        <div class="header">
            <div class="number">{q['num']}</div>
        </div>
        
        <div class="content">
            <div class="title">
                <span class="title-1">{q['title_1']}</span> <span class="title-2">{q['title_2']}</span>
            </div>
            
            <div class="body-grid">
                <div class="body-left">
                    {q['body_left']}
                </div>
                <div class="body-right">
                    {q['body_right']}
                </div>
            </div>
        </div>
        
        <div class="footer">
            <div class="footer-left">FAQ</div>
            <div class="footer-center">Nguyễn Đức Việt<span>0934.688.632</span></div>
            <div class="footer-right">2026</div>
        </div>
    </div>
    """

html_content += """
</body>
</html>
"""

with open('tui-mu.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Đã tạo file tui-mu.html thành công!")
