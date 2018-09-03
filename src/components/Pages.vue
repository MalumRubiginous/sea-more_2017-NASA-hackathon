<template>
    <div>
        <Content :pageIndex="this.pageIndex"/>
    </div>
</template>

<script>
    import Content from './Content.vue';
    export default {
        props: ['pageIndex'],
        components: {
            Content
        }
    }
</script>

<style lang="css">

</style>
