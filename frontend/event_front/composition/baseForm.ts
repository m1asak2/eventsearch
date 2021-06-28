import { DisplayForm, SendForms } from '@/types/interfaces'
import { defineComponent, reactive, toRefs } from '@nuxtjs/composition-api'

function ToSendForm(data: DisplayForm) {
  const ToSend = reactive<SendForms>({
    keyword: data.keyword.split(' '),
    address: data.address.split(' '),
    start_from: data.start_from,
    start_to: data.start_to,
    limit: data.limit,
    target: data.target
  })
  return toRefs(ToSend)
}

const ToDisplayForm = (data: SendForms) => {
  const ToDisplay = reactive<DisplayForm>({
    keyword: data.keyword.join(' '),
    address: data.address.join(' '),
    start_from: data.start_from,
    start_to: data.start_to,
    limit: data.limit,
    target: data.target
  })
  return toRefs(ToDisplay)
}

export default defineComponent({
  setup() {
    const sendform = reactive<SendForms>({
      keyword: [],
      address: [],
      limit: 0,
      start_from: '',
      start_to: '',
      target: []
    })
    const displayform = reactive<DisplayForm>({
      keyword: '',
      address: '',
      limit: 0,
      start_from: '',
      start_to: '',
      target: []
    })

    const ToSend = ToSendForm(displayform)
    const ToDisplay = ToDisplayForm(sendform)
    return {
      ToSend,
      ToDisplay,
      sendform,
      displayform
    }
  }
})
