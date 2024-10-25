console.log('OLAAAA')

const socket = new WebSocket('ws://' + window.location.host + '/ws/metricas');

const callbacksNaoProcessados = document.getElementById('callbacks_n_processados')

const limitCallbacksNaoProcessados = 500

const limitAtencaoCallback = 300

const limitPossivelErroFilaCallbacks = 450 

const coresAlertasCallbacks = {
    'normal': {
        'cor_barra': 'bg-green-600',
        'cor_text': 'text-green-600',
        'text': 'Tudo certo...'
    },
    'atencao':  {
        'cor_barra': 'bg-yellow-600',
        'cor_text': 'text-yellow-600',
        'text': 'Atenção...'
    },
    'possivel_erro':  {
        'cor_barra': 'bg-red-600',
        'cor_text': 'text-red-600',
        'text': 'Possível problema detectado!'
    }
}

socket.onmessage = function(e) {
    console.log(e)
    console.log('Server: ',  JSON.parse(e.data));
    data_info = JSON.parse(e.data)
    callbacksNaoProcessados.textContent = data_info.callbacks_count

    var bar = document.getElementById("progress-bar");
    var barMessage = document.getElementById("progress-bar-message");
    barMessage.textContent = ''
  
    if (parseInt(data_info.callbacks_count) >= limitAtencaoCallback && parseInt(data_info.callbacks_count) < limitPossivelErroFilaCallbacks){ 
        console.log('PRIMEIRO CASE')
        bar.classList.remove(coresAlertasCallbacks['normal']['cor_barra'])
        bar.classList.remove(coresAlertasCallbacks['possivel_erro']['cor_barra'])
        bar.classList.add(coresAlertasCallbacks['atencao']['cor_barra'])

        barMessage.classList.remove(coresAlertasCallbacks['normal']['cor_text'])
        barMessage.classList.remove(coresAlertasCallbacks['possivel_erro']['cor_text'])

        barMessage.textContent = coresAlertasCallbacks['atencao']['text']
        barMessage.classList.add(coresAlertasCallbacks['atencao']['cor_text'])

    } else if (parseInt(data_info.callbacks_count) >= limitPossivelErroFilaCallbacks) {
        console.log('SEGUNDO CASE')
        bar.classList.remove(coresAlertasCallbacks['normal']['cor_barra'])
        bar.classList.remove(coresAlertasCallbacks['atencao']['cor_barra'])
        bar.classList.add(coresAlertasCallbacks['possivel_erro']['cor_barra'])

        barMessage.classList.remove(coresAlertasCallbacks['normal']['cor_text'])
        barMessage.classList.remove(coresAlertasCallbacks['atencao']['cor_text'])

        barMessage.textContent = coresAlertasCallbacks['possivel_erro']['text']
        barMessage.classList.add(coresAlertasCallbacks['possivel_erro']['cor_text'])

    } else {

        console.log('TERCEIRO CASE')
        bar.classList.remove(coresAlertasCallbacks['possivel_erro']['cor_barra'])
        bar.classList.remove(coresAlertasCallbacks['atencao']['cor_barra'])
        bar.classList.add(coresAlertasCallbacks['normal']['cor_barra'])


        barMessage.classList.remove(coresAlertasCallbacks['possivel_erro']['cor_text'])
        barMessage.classList.remove(coresAlertasCallbacks['atencao']['cor_text'])

        barMessage.textContent = coresAlertasCallbacks['normal']['text']
        barMessage.classList.add(coresAlertasCallbacks['normal']['cor_text'])

    }

    var progresso_porcentagem = (parseInt(data_info.callbacks_count) * 100) / limitCallbacksNaoProcessados
    bar.style.width = progresso_porcentagem + "%"
    bar.textContent = parseFloat(progresso_porcentagem).toFixed(2) + "%"
};

socket.onopen = function (e) {
    // socket.send(JSON.stringify({
    //     'message': 'Ola do cliente',
    //     'sender': 'raul cliente'
    // }))
}