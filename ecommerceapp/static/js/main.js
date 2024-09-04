function addtoacrt(id)          // تنفذ مهمه السله بدون ان تعيد الى الصفحه
{
      var cart=document.getElementById('cart')         //'cart' is the name of id from base page
    var ajaxurl="/add_to_cart/";                //url
    $.ajax({

        headers: { "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content") },
        url:ajaxurl,
        data:{id:id},
        method:"post",

        success:function(response){                 // بعد تنفيذ الداله في الباك ايند يقوم ينفذ السكساس
            cart.innerHTML=response.count          // هذا كلو عشان احدث الارقام اللي فوق السله بدون ما اضطر الى تحديث السله 
            Swal.fire({                            // تظهر رساله للمستخدم 
                position: "top-end",
                icon: "success",
                title: "تم الإضافة الى السلة بنجاح",
                showConfirmButton: false,
                timer: 1500
              });
          
        }

    });
}