class Errors {
  constructor() {
    this.errors = {}
  }

  has(field) {
    return this.errors.hasOwnProperty(field)
  }

  any() {
    return Object.keys(this.errors).length > 0
  }

  get(field) {
    if (this.errors[field]) {
      return this.errors[field][0]
    }
  }

  record(errors) {
    this.errors = errors
  }

  clear(field) {
    if (field) {
      delete this.errors[field]

      return
    }

    this.errors = {}
  }
}

class Form {
  constructor(data) {
    this.originalData = data

    for (let field in data) {
      this[field] = data[field]
    }

    this.errors = new Errors()
  }

  data() {
    let data = {}

    for (let property in this.originalData) {
      data[property] = this[property]
    }

    return data
  }

  reset() {
    for (let field in this.originalData) {
      this[field] = ''
    }

    this.errors.clear()
  }

  // /**
  //  * Send a POST request to the given URL.
  //  * .
  //  * @param {string} url
  //  */
  // post(url) {
  //   return this.submit('post', url)
  // }

  // /**
  //  * Send a PUT request to the given URL.
  //  * .
  //  * @param {string} url
  //  */
  // put(url) {
  //   return this.submit('put', url)
  // }

  // /**
  //  * Send a PATCH request to the given URL.
  //  * .
  //  * @param {string} url
  //  */
  // patch(url) {
  //   return this.submit('patch', url)
  // }

  // /**
  //  * Send a DELETE request to the given URL.
  //  * .
  //  * @param {string} url
  //  */
  // delete(url) {
  //   return this.submit('delete', url)
  // }

  // /**
  //  * Submit the form.
  //  *
  //  * @param {string} requestType
  //  * @param {string} url
  //  */
  // submit(requestType, url) {
  //   return new Promise((resolve, reject) => {
  //     axios[requestType](url, this.data())
  //       .then(response => {
  //         this.onSuccess(response.data)

  //         resolve(response.data)
  //       })
  //       .catch(error => {
  //         this.onFail(error.response.data)

  //         reject(error.response.data)
  //       })
  //   })
  // }

  // /**
  //  * Handle a successful form submission.
  //  *
  //  * @param {object} data
  //  */
  // onSuccess(data) {
  //   alert(data.message) // temporary

  //   this.reset()
  // }

  // /**
  //  * Handle a failed form submission.
  //  *
  //  * @param {object} errors
  //  */
  // onFail(errors) {
  //   this.errors.record(errors)
  // }
}

export {Errors, Form}
