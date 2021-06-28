import { DisplayForm, SendForms } from '@/types/interfaces'

export const ToSendForm = (data: DisplayForm) => {
  const ToSend: SendForms = {
    keyword: data.keyword.split(' '),
    address: data.address.split(' '),
    start_from: data.start_from,
    start_to: data.start_to,
    limit: data.limit,
    target: data.target
  }
  return ToSend
}
