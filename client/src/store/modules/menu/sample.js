import lazyloading from '@/utils/lazyLoading'

const searchBox = {
  text: '검색Bar',
  path: '/example/searchbox',
  component: lazyloading('example/searchbox')
}

const tabs = {
  text: '탭',
  path: '/example/tab',
  component: lazyloading('example/tab')
}

export default [{
  text: '테스트',
  icon: 'toc',
  pri: 1200,
  model: false,
  children: [searchBox, tabs]
}]
