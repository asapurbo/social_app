const emoji = [...'😀😃😄😁😆🥹😅😂🤣🥲😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳😏😒😞😔😟😕🙁☹️😣😖😫😩🥺🤗🤔🫣🤭🫢🫡🫡🤫🫠🤥😶🫥🫨😐🫤😑😬🙄😯😦😧😮😲🥱😴🤤😪😮‍💨😵😵‍💫🤐🥴🤢👽👾🤖🎃😺😸😹😻😼😽🙀😿😾🫶🤲👐🙌👏🤝👍👎👊✊🤛🤜🤞✌️🫰🤟🤘👌🤌🤏🫳🫴🫷🫸👈👉👆👇☝️✋🤚🖐🖖👋🤙👅👂🧒👦👩🧑👨👩‍🦱🧑‍🦱👨‍🦱']

const emoji_container = document.getElementById('emoji_container')
const textarea = document.getElementById('textarea')
const btn = document.getElementById('btn')

emoji_container.innerHTML = emoji.map((e) => `<span style='cursor: pointer'; class='emoji'>${e}</span>`).join('')

btn.addEventListener('click', () => {
    navigator.clipboard.writeText(textarea.value)
    emoji_container.style.display = emoji_container.style.display === 'block' ? 'none' : 'block'
})

emoji_container.querySelectorAll('.emoji').forEach((e) => {
    e.addEventListener('click', () => {
        textarea.value+=e.textContent
    })
})

document.addEventListener('click', (e) => {
    if(!emoji_container.contains(e.target) && !btn.contains(e.target)) {
        emoji_container.style.display = 'none'
    }
})

