from dishka import Provider, provide, Scope


class CategoryUseCasesProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_cate