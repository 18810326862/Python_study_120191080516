function goonclick() {

    form1 = document.getElementById('form1');
    form1.submit();
}

function doonclick(obj, id) {
    /* if (document.getElementsByName(elementname).value == 'Undo'){
         document.getElementsByName(elementname).value = 'Done';
     }
     else{
         document.getElementsByName(elementname).value = 'Undo';
     }*/
    var name = 'title' + id;

    if (obj.value == 'Undo') {
        obj.value = 'Done';

        var title = document.getElementsByName(name);
        for (var i = 0; i < title.length; i++) {
            title[i].style["textDecoration"] = 'None';
        }
    } else {
        obj.value = 'Undo';

        var title = document.getElementsByName(name);
        for (var i = 0; i < title.length; i++) {
            title[i].style["textDecoration"] = 'line-through';
        }

    }

     form2 = document.getElementById('form2')
     form2.action = "/done/" + id;
     form2.submit();


}

function editonclick(obj, id) {
    /*if(document.getElementsByName(elementname).value == 'Edit'){
        document.getElementsByName(elementname).value = 'Save';
    }
    else{
        document.getElementsByName(elementname).value = 'Edit';

    }*/
    if (obj.value == 'Edit') {
        var name = 'title' + id;
        var edit = document.getElementsByName(name)
        for (var i = 0; i < edit.length; i++) {
            edit[i].readOnly = false;
        }
        obj.value = 'Save';
    } else {
        var name = 'title' + id;
        var edit = document.getElementsByName(name)
        for (var i = 0; i < edit.length; i++) {
            edit[i].readOnly = true;
        }
        obj.value = 'Edit';
        form2 = document.getElementById('form2')
        form2.action = "/update/" + id;
        form2.submit();
    }

}

function removeonclick(obj, id) {
    var form = document.getElementById('form2');
    form.action = "/remove/" + id;
    form.submit();


}

window.onload = function () {
    document.getElementsByName("search")[0].focus();
    //document.getElementsByName("search")[0].setSelectionRange(this.value.length,this.value.length);
}


// function setFocus(obj)
// {
// //var obj = event.srcElement; //获得焦点对象
// //var txt =obj.setSelectionRange(obj.value.length,obj.value.length);
// // var txt = obj.createTextRange();// 用createTextRange来创建Range对象操作文本不行
// // txt.moveStart('character',obj.value.length); //修改文档的开始节点，向后移动长度
// // txt.collapse(true);
// // txt.select();
//     obj.focus();
//     obj.setSelectionRange(obj.value.length,obj.value.length);
// }
