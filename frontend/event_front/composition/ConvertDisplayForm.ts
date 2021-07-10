import { DisplayForm, SendForms } from '@/types/interfaces'

export const DisplayToSendForm = (data: DisplayForm) => {
  const ToSend: SendForms = {
    keyword: data.keyword.split(' '),
    address: data.address.split(' '),
    start_from: data.start_from,
    start_to: data.period,
    limit: data.limit,
    target: data.target
  }
  return ToSend
}
