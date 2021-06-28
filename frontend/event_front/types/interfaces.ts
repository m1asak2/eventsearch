export type SendForms = {
  keyword: string[]
  address: string[]
  limit: number
  // eslint-disable-next-line camelcase
  start_from: string
  // eslint-disable-next-line camelcase
  start_to: string
  target: string[]
}

export type EventData = {
  day: string
  time: string
  title: string
  address: string
  img: string
  group: string
  link: string
}

export type DisplayForm = {
  keyword: string
  address: string
  limit: number
  // eslint-disable-next-line camelcase
  start_from: string
  // eslint-disable-next-line camelcase
  start_to: string
  target: string[]
}
