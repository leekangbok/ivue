import lazyloading from '@/utils/lazyLoading'

const viewChart = {
  text: 'View Chart',
  path: '/bitcoin/ViewChart',
  component: lazyloading('bitcoin/ViewChart')
}

const intro = {
  text: 'Why ?',
  path: '/bitcoin/Intro',
  component: lazyloading('bitcoin/Intro')
}

export default [{
  text: '비트코인',
  icon: 'toc',
  pri: 700,
  model: true,
  children: [intro, viewChart]
}]
