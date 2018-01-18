import lazyloading from '@/utils/lazyLoading'

const product = {
  text: '소프트웨어',
  path: '/qna/software',
  component: lazyloading('qna/software')
}

const tech = {
  text: 'Tech',
  path: '/qna/tech',
  component: lazyloading('qna/tech')
}

export default [{
  text: 'Q&A',
  icon: 'toc',
  pri: 800,
  model: false,
  children: [tech, product]
}]
