Giải này thì chính thức mình chẳng giải được bài mịa nào =))) hết giải mới nhận ra là lỗi này mình làm rồi nên chốt câu mình còn gà vl :(( 

![image]()

đây là đoạn code quan trọng nhất của cả chương trình và cũng là đoạn duy nhất. Nhìn vào ban đầu mình nghĩ nó là prototype pollution do nó cho thêm object tùm lum mà hầu như không kiểm soát. Thử build lên chạy thì trong thư viện fast-json-patch có chặn \_\_proto\_\_ tuy nhiên mình có thể bypass bằng cách dùng constructor.prototype hay như đối với bàu này thì input sẽ kiểu /constructor/prototype/???. Mình mắc kẹt ở đây đến hết giải do không tìm được gadget để RCE đọc đi đọc lại thử đi thử lại cũng không thấy. Đến hết 1 ngày thì mình nghĩ chắc éo phải prototype đâu và bỏ cuộc do không tìm được hướng nào khác.
Tuy nhiên khi giải kết thúc mình bị vả một phát đau đcđ 
![image]()

Gadget nằm trong thư viên khác .... và khi mình mở thư viện đó lên và xem hàm bị lỗi thì ...
![image]()

Dạ vâng nó là lỗi khi render 1 template giống với lỗi trong thư viện handlebar.js đây là một lỗi mình đã từng phân tích ở chỗ thực tập đã thế còn làm báo cáo hẳn hoi mới cay :((. Về cơ bản khi render thì ở hàm outputFunctionName trong ejs sẽ tạo ra 1 constructor dựa trên input và input này không được escape dẫn đến việc mình có thể thực hiện chèn thêm code vào và dẫn đến RCE(tham khảo https://github.com/mde/ejs/issues/451).
Viết đến đây thôi mình trầm cảm tiếp đây :(