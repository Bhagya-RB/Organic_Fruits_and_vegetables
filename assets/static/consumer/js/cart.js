var updateBtns = document.getEmenetsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId =this.dataset.productId
        var action = this.dataset.action
        console.log('productID;',productId, 'action:',action)

        console.log('CONSUMER:',consumer)
        if (consumer == 'Anonymousconsumer'){
            console.log('Consumer is not authenticated')
        }else{
            console.log('Consumer is authenticated, sending dats...')
        }
    })
}