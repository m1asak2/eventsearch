import { DisplayForm, SendForms } from '@/types/interfaces'

export const ToDisplayForm = (data: SendForms) => {
  const ToDisplay: DisplayForm = {
    keyword: data.keyword.join(' '),
    address: data.address.join(' '),
    start_from: data.start_from,
    start_to: data.start_to,
    limit: data.limit,
    target: data.target
  }
  return ToDisplay
}
