import lazyloading from '@/utils/lazyLoading'

export default [{
  text: '미디어',
  path: '/liveStream',
  icon: 'live_tv',
  pri: 301,
  component: lazyloading('liveStream', true)
}]
