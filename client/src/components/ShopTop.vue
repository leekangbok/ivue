<template>
  <iu-toolbar-nav title="DSHOP"
    height="28px">
    <div class="d-flex align-center"
      style="margin-left: auto">
      <LogInOut/>
      <MoreApps></MoreApps>
    </div>
  </iu-toolbar-nav>
</template>

<script>
import MoreApps from './MoreApps'
import Notifications from './Notifications'
import Accounts from './Accounts'
import LogInOut from './LogInOut'

export default {
  data() {
    return {}
  },
  components: {
    MoreApps,
    Notifications,
    Accounts,
    LogInOut
  }
}
</script>
