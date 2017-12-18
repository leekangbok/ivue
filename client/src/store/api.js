import axios from 'axios'

export default {
  request(method, url, config = {}, callback = () => {}, errback = () => {}) {
    return new Promise((resolve, reject) => {
      axios[method](url, config)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  get(url, config = {}, callback = () => {}, errback = () => {}) {
    return new Promise((resolve, reject) => {
      axios
        .get(url, config)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  post(url, config = {}, callback = () => {}, errback = () => {}) {
    return new Promise((resolve, reject) => {
      axios
        .post(url, config)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  put(url, config = {}, callback = () => {}, errback = () => {}) {
    return new Promise((resolve, reject) => {
      axios
        .put(url, config)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  },
  delete(url, config = {}, callback = () => {}, errback = () => {}) {
    return new Promise((resolve, reject) => {
      axios
        .delete(url, config)
        .then(response => {
          callback(response)
          resolve(response)
        })
        .catch(error => {
          errback(error)
          reject(error)
        })
    })
  }
}
