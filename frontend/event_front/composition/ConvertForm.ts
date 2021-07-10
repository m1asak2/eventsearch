import { DisplayForm, SendForms, SaveForm } from '@/types/interfaces'
import { getDate, getDateDay } from '@/composition/GetDate'
export const DisplayToSendForm = (data: DisplayForm) => {
  const ToSend: SendForms = {
    keyword: data.keyword.split(' '),
    address: data.address.split(' '),
    start_from: data.start_from,
    start_to: getDateDay(data.start_from, Number(data.period)),
    limit: data.limit,
    target: data.target
  }
  return ToSend
}

export const SendToDisplayForm = (data: SendForms) => {
  const ToDisplay: DisplayForm = {
    keyword: data.keyword.join(' '),
    address: data.address.join(' '),
    start_from: data.start_from,
    period: data.start_to,
    limit: data.limit,
    target: data.target
  }
  return ToDisplay
}
export const SaveToDisplayForm = (data: SaveForm) => {
  const ToDisplay: DisplayForm = {
    keyword: data.keyword,
    address: data.address,
    start_from: getDate(),
    period: data.period,
    limit: data.limit,
    target: data.target
  }
  return ToDisplay
}

export const DisplayToSaveForm = (data: DisplayForm) => {
  const ToSend: SaveForm = {
    keyword: data.keyword,
    address: data.address,
    period: data.period,
    limit: data.limit,
    target: data.target
  }
  return ToSend
}
