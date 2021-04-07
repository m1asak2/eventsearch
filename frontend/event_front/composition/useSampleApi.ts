import { toRefs, reactive } from '@nuxtjs/composition-api'
import { NuxtAxiosInstance } from '@nuxtjs/axios'
import useApi from '~/composition/useApi'
type eventData = {
  day: string
  time: string
  title: string
  address: string
  img: string
  group: string
  link: string
}
type GetForm = {
  keyword: string
  address: string
  limit: number
  // eslint-disable-next-line camelcase
  start_from: string
  // eslint-disable-next-line camelcase
  start_to: string
}
type baseState = {
  response: eventData[]
  error: Error | null
  isLoading: boolean
}

export default (axios: NuxtAxiosInstance) => {
  const sampleState = reactive<baseState>({
    response: [],
    error: null,
    isLoading: false
  })
  const apiPostTrigger = async (data: GetForm) => {
    const { response, otherError, isLoading, postData } = useApi(
      axios,
      // 'http://192.168.56.1:8000/api/v01/connpass'
      '/api/connpass'
    )
    sampleState.isLoading = isLoading as any
    await postData(data)
    sampleState.response = response as any
    sampleState.error = otherError as any
  }
  return {
    ...toRefs(sampleState),
    apiPostTrigger
  }
}
