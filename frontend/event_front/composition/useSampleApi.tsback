import { toRefs, reactive } from '@nuxtjs/composition-api'
import { NuxtAxiosInstance } from '@nuxtjs/axios'
import { EventData, DisplayForm } from '@/types/interfaces'
import useApi from '@/composition/useApi'

type baseState = {
  response: EventData[]
  error: Error | null
  isLoading: boolean
}

export default (axios: NuxtAxiosInstance) => {
  const sampleState = reactive<baseState>({
    response: [],
    error: null,
    isLoading: false
  })
  const apiPostTrigger = async (data: DisplayForm) => {
    const { response, otherError, isLoading, postData } = useApi(axios, '/api')
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
